import copy
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import simpledialog
from tkinter import messagebox

from ttkbootstrap.themes import standard
from view import link_window


class QuickAccessTreeview(ttk.Treeview):
	def __init__(self, view, nodes=['Default']):
		super(QuickAccessTreeview, self).__init__(view.sidebar_frame, selectmode='browse', show="tree")
		self.view = view
		
		# #bind left click event
		self.bind('<<TreeviewSelect>>',lambda event, : self.single_click(event))
		self.bind("<Button-3>",lambda event,: self.on_right_click(event))
		self.bind("<Motion>", self.highlight_row)
		self.bind("<Leave>", self.leave_treeview)

		self.close_btn = tk.Button(view.sidebar_frame, image=self.view.close_icon2, background="white", relief=FLAT,
				command= lambda action=False: self.open_close_all_nodes(action))
		self.close_btn.grid(row=1, column=0, sticky="w", padx=0)
		self.up_btn = tk.Button(view.sidebar_frame, image=self.view.up_icon2, background="white", relief=FLAT,
				command=self.move_up)
		self.up_btn.grid(row=1, column=1, sticky="w", padx=0)
		self.down_btn = tk.Button(self.view.sidebar_frame, image=self.view.down_icon2, background="white", relief=FLAT,
				command=self.move_down)
		self.down_btn.grid(row=1, column=2, sticky="w", padx=0)
		
		self.update_btn_bg()
		self.update_tags()
		
	def update_btn_bg(self):
		s = ttk.Style()
		bg = s.lookup("TFrame", "background")
	
		self.close_btn.config(bg=bg)
		self.up_btn.config(bg=bg)
		self.down_btn.config(bg=bg)

	def update_tags(self):
		highlight_color = standard.STANDARD_THEMES[self.view.style_name]["colors"]["active"]
		self.tag_configure('highlight', background=highlight_color)
		
	def highlight_row(self, event):
		item = self.identify_row(event.y)
		item = f'"{item}"'
		self.tk.call(self, "tag", "remove", "highlight")
		self.tk.call(self, "tag", "add", "highlight", item)
			
	def insert_new_folder(self, folder_id, text, idx=0):
		self.insert("", idx, iid=folder_id, text=text, image=self.view.folder_icon2)

	def rename_folder(self, folder_id, text):
		self.item(folder_id, text=text)
		
	def single_click(self, event, click='single'):
		if click == 'single':
			item_iid = event.widget.selection()[0]
			parent_iid = event.widget.parent(item_iid)
			
			if parent_iid: #if it is a link and not a node
				current_root_tab = self.view.main_notebook.nametowidget(self.view.main_notebook.select())
				current_branch_tab = current_root_tab.notebook.nametowidget(current_root_tab.notebook.select()).branch_id
				self.view.controller.link_clicked(parent_iid, item_iid, current_branch_tab)
					
	def on_right_click(self, event):
		self.unbind("<Button 1>")
		# select row under mouse
		iid = self.identify_row(event.y)
		if iid:
			# mouse pointer over item
			self.selection_set(iid)
			self.bind('<<TreeviewSelect>>',lambda event, click='right': self.single_click(event, click))
			
		popup_menu = tk.Menu(event.widget, tearoff=0)
		popup_menu.add_command(label="Add New Folder", command=self.view.controller.add_new_quick_access_folder, image=self.view.folder_icon2, compound="left",)
		
		if len(event.widget.selection()) > 0:
			item_iid = event.widget.selection()[0]
			parent_iid = event.widget.parent(item_iid)
			
			if not parent_iid: #if it is a node and not a link
				popup_menu.add_command(label="Rename Folder", command=lambda folder_id=item_iid: self.view.controller.rename_quick_access_folder(folder_id), image=self.view.edit_icon2, compound='left',)
				popup_menu.add_command(label="Delete Folder", command=lambda folder_id=item_iid: self.view.controller.delete_quick_access_folder(folder_id), image=self.view.delete_icon2, compound="left",)
				popup_menu.add_separator()
				popup_menu.add_command(label="Add New Link", command=lambda folder_id=item_iid, mode='new': self.view.controller.add_new_link(folder_id, mode), image=self.view.new_link_icon2, compound='left',)
			else:
				popup_menu.add_separator()
				popup_menu.add_command(label="Edit Link", command=lambda folder_id=parent_iid, link_id=item_iid: self.view.controller.edit_link(folder_id, link_id), image=self.view.edit_link_icon2, compound="left",)
				popup_menu.add_command(label="Delete Link", command=lambda folder_id=parent_iid, link_id=item_iid: self.view.controller.delete_link(folder_id, link_id), image=self.view.delete_link_icon2, compound='left',)
		
		try:
			popup_menu.tk_popup(event.x_root, event.y_root, 0)
		finally:
			popup_menu.grab_release()
		
		self.bind('<<TreeviewSelect>>',lambda event, click='single': self.single_click(event, click))
	
	def launch_new_link_window(self, master, mode, text=None, path=None):
		self.w = link_window.AddLinkWindow(master, mode, text=text, path=path)
		master.wait_window(self.w.top)
	
		if self.w.button == "ok":
			text = self.w.name
			path = self.w.path
			
		return text, path
	
	def insert_new_link(self, folder_id, link_id, text):
		self.insert(folder_id, "end", iid=link_id, text=text)
		
	def update_link(self, link_id, text):
		self.item(link_id, text=text)

	def delete_folder(self, folder_id):	
		self.detach(folder_id)
			
	def delete_link(self, link_id):
		self.detach(link_id)

	def open_close_all_nodes(self, action):
		for node in self.get_children():
			self.item(node, open=action)

	def move_up(self):
		leaves = self.selection()
		for i in leaves:
			self.move(i, self.parent(i), self.index(i)-1)
		
		self.update_links_order()

	def move_down(self):
		leaves = self.selection()
		for i in leaves:
			self.move(i, self.parent(i), self.index(i)+1)

		self.update_links_order()
			
	def update_links_order(self):
		quick_access_order = {}
		for folder_id in self.get_children():
			quick_access_order[folder_id] = []
			
			for link_id in self.get_children(folder_id):
				quick_access_order[folder_id].append(link_id)
		
		self.view.controller.update_quick_access_order(quick_access_order)

	def leave_treeview(self, event):
		self.tk.call(self, "tag", "remove", "highlight")
		

			

		
		