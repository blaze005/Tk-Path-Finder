from PIL import Image, ImageTk
import base64
import io

def setup_icons(mainapp):

	size = 18,18

	data = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAABfklEQVRoge2XPUvDUBSG39h84CyU1ioOMXToIDWCf8Ctf8DBTfE3ODYogoOIg4MOgoi/xN3FRRARdNChflBQ8tHkOhVyAzVgjmkTzgMZTnJ5733uPQkEYBiGYTKgxIuXS3QU4FQAjT/mCQD3ULBf38BF9uWlIwk8neMZwBxFsBBwFjbRpcj6DUng4QyCOP/A3MYOcaaEJHB3Qi4AARxFBvZaW3inzgYSArfH9AJV00bVXAEUJX1wCgP3O+z3Hp2Ztevd4T0p9eaQVqBu2ahZNmUkAvcr1NtX6rBWpYcB3USN5jJqi21ARHShADRjuhKvZYFB9glU3cB8cwmzVgtAmD0wbb54sdpZh6obNMnEOz8KSUDVtNwmpkKVy2ItHkgKFGz3AT6B8VMyAW6h/CmZQNFbSPAJ5E/J3oHCC3AL5U9C4P//oKjhFho3JRPgFsqfcp2A73qhbmiVUYMnAd8NpG/9VLz4eO07vuuFEBEm8fJdL+y9fXZz3TGGYZhy8wPLqL/TAN/hMAAAAABJRU5ErkJggg=='
	mainapp.folder_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))

	data = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABmJLR0QA/wD/AP+gvaeTAAACxUlEQVRIidWXS2gTURSG/8m8Mkk6maQvlWhJU7WFWqtVoUpFhIALF10YcFFEl66K4MJNISjYTRHURelGKmKFuhAUBCl24VZU0KZg0zR9JE3b1GTiZJLahBkXNW3TxHbyqMV/deecM+e759wLhwvskYithicv310WeOPFQhOJUpyeHQv1uN03xKJ2MvR69JFahL77A+rTVyPRO73PLVo4uqJ2l0cUqcOljlPCyeM2760Hw9Z/BgYAmqLQ6TxX2d5YO7ETvKzgNTipCV52sFZ4WcGiFEckJiESkyDJCZw/fayy1W7x5btwVLmg+6utCC7+QESUsuxnWhqFZGL1PoCbuwLm9Cwa6g7k9X3xeFNbbbtyxlq0Z2BNrf405i0oaVvz4fKAtSQqVGWruNDN/f8VA4BKEFCgwGAhEBBD0IEAQzGgK+iWosBaK/44/RUT4UkYSRYmIwcASCorkIzRdvfbhy98y3Pdz671LWkGT82FtvWn0ipmViYhExJqa4QsH6UjYaupYmzVVVdN01yjMHjvyuPrPT5NYAtfsa3/c8ADmZRg4riNf/QWWPUCfKJ/zUAALXZHayq1Ougadl3QBjab/upTVAWh5Dxqq81ZdqteQL3ZvgH+o2Z7w1nxW7y75Ms1K4VgEGgtaQAALE3rrDzvLPlyhcdDIA0GABvtzawBwCHY12Mz1bM0e6jk6aSqyvo6097N2vydARM6gi0ZzDEGJJUYKB0Jn+hfT+4Q7Kg32zEyM5rzTzqdjpQ8nU7YmnKG/06KJxJjJYPNXAX04ABVW3wgvLQwHxX7yjKPnU0dWAhnPyB8oj+nzfFk4pc3GOwf6HKP55zxT1n+MPTmPVsImKEZI8tUHfHEpo466vbxeobJiQmElxa8wWB/b+ftu0Cet1Mpcg27yHqqrdvK806O1R9UVJVTFGVZkmXPfFTsG+hyj2difwPxFi1bPxhiJQAAAABJRU5ErkJggg=='
	mainapp.new_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))

	data='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'
	mainapp.word_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))

	data ='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'
	mainapp.excel_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))

	data = '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'
	mainapp.pdf_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))

	data = 'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAEP0lEQVR4nO3cW1MaZxzH8R9ECUZADuHsGqyJaPWi6USb6fTOmbyHvoL2HbT3vWnfQXKdF9GZTC87k6qZSacmHjqmIngABRERoxZ2e5Fk2Uc0EQb2v0/3/7lyH3aXlS8Ph1UAGGOMMcbsyNGtHT37/g+tW/syheb45dGTr36kPgwn9QGQcWg/PPtu/mfqw7BvAMASEWwX4M5cTBwgjmC7AImvw5aKYLsAgLUi2DIAYJ0Itg0AWCOCrQMA9BFsHwCgjcAB3qOKwAEMKCJwgAvMjsABLmFmBA5wBbMicICPMCMCB/iEXkfgANfQywgc4Jp6FYEDtKEXEThAm66K0On+OEAHLo3Qob6u7EUiz39aoj4EAc8AYhyAGAcgxgGIcQBiHIAYByDGAYhxAGIcgBgHIMYBiHEAYhyAGAcgxgGIcQBipv9FLJMv49eFtba3m51QMHUngqe/vUS9oerj9+8m8PDzEWHdP9d38Hw5qy874cC3c19gs1DG768ybV/33Jd3MT58u+3trsP0AKqq4ey83vZ29YYK981+jCVC+OvNrj6+9E8esxMKnM7mZ86XNvLCdYwrYfgGb6Kuqh1dd8MQvNukewiaSSdxw3Bj107PkSmU9eXdUhWlyknLNlZl+gwI+m7hm+mUMLZVrCCTb96I8ZAXY/GQsE4yPAQA8N5yI62Esby5p1/2aiOPz+JB/Wej0VgAYb8HAJAI+Vque32nhPxBtbl+PIhkyCesE3m/fS+YHsDvcePBxLA4uAohQDTgbV3HYGZCwXJ2H9DefT1FJl9G7e05+vv78PdWUVj3waRi2K8H0YB4Yx6dnAkBRiJDuH/PvBkj3UMQAAS8AxhLNGeIqmp4vVnAWnYP/9Yb+ng85Gu5N1uNtP8XNJNO4s12897+eqMAt0v8dWYN936rknIGAEAs6MVI1K8vV2qnKJSP9eXbQ4NIxQIUh9YWaQMAwEz66ueJ2Umle1+G1ENSB1AifsRD3pZxv8eNe8nevHHqNqkDAEC90fpFXQ1Vg6b17s1TN0kdYGP3APuHxy3j1ZMzrGT3CY6ofVIHeLG6deVli6u5D28TLE3aAFv7R9guHenLfs8AYsHm88Hh8SnWt4uXbWop0gZYXMsJy9OpKKZHxQ9NzK/kYPVJIGWAvcMasoZTF06nA5OpCMaVMFz9N/TxYqWGTcN6ViRlgIWVrHDPHo2HMOh2wdXnRHo4LKw7vyLOFKuRLkC5+hbrOwfC2HQq0vz5wsPQbukIO8WKKcfWCekCLK7mYHx54xlwIRUL6svRoEc//fzBwkdeLVGTKkD15BRrOfH1/VQqCseFcw5ThhkBvDtdbTxPZCX2/e7oLnv0+GFHt6VUM+D/iAMQ4wDEOAAxDkCMAxDjAMQ4ADEOQIwDEOMAxDgAMQ5AjAMQ4wDEOAAxDkCMAxDjAMQ4ADEOQIwDEOMAjDHGGGOMwH+t2FX1CofvaAAAAABJRU5ErkJggg=='
	mainapp.text_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))
	
	data='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'
	mainapp.python_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))

	data = 'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAD8ElEQVR4nO3cX08TWRzG8WemLAg0+Ce4emGMF2a9qF66eqMx8Q15t/sS1jvfCanJqtGsgMRoW5QYp4lYkbWsbaG1bKkUW9qZvdAiwrSdzmnndzbzfK5gOj0d+GbmzAm0ABEREVEYGaoD3EnWnUEcSGAM3L51eex36cNoM6UPIHAOfruTqv8hfRht4QsAaBUhNAFipw78qJpECE2AX6YjWkYITQBAzwihCgDoFyF0AQC9IoQyAKBPhNAGAPSIEOoAgHyE0AcAZCMwwDdSERhgH4kIDHBA0BEYwEWQERigg6AiMEAXQURggB6GHYEBPBhmBAbwqFME1XEZoA+uERSNDHQ0jc2kd6UPwRXPAGEMIIwBhDGAMAYQxgDCGEAYAwhjAGEMIIwBhDGAMAYQxgDCGEAYAwhjAGH/i7+IWSslGA4QOz+tPJZtO3hilZDOVgDDQOzsFK7HpmGaym+Z9kX7ANVaAw+frsJ2gDOnp3A0Oqo03pN0CYm35b3vE8tfv75x6aTSuH5pfQlyHODubAY79SbqjSbisxnYjtob89MfKp62BUXrAInXOfyd29r7fq2whaRVUBvUcLnUuG0LiLYBSps1zC+uHdo+l8pivbzte9zY2alD2y66bAuKlgFaLRszjzNotmzXx+J/uT/mxfXYNK5cOIHo+Aii4yO4cuEErsXUJ3e/tJyEZ1NZbJRrHR8v/ruD+VQWN6+e6zpOe74w911iTNPAjUsnxSbdg7Q7A7KFLSStfM/9Elb+h/nBzYJVwkK6NKhDGwqtAnypN3F3NgMvNzr775DcrOS3kXhbRmK5jEzu84CPdHC0CvDg6Soqnxue96/WGri38N5lexN/LhbgOF9D3UsVUKnxXxO7slZKSK/0f7l4s/oJ6Xffn9eyHcSTuR/OjC+7LcSf52Hb+n24lxYB2qtdv+7vO3PmXhfxsbRzaJ98eQdzVtH3awyLeIBe13Iv2qvkTK6KF+82O+63mNnE8j9V368zDOK3oQdXu36tbWyjmMh3ncAdB7j/ch0/HzuC49GflF9zEETPgE6r3f4ZiExOotnqfY2vN1qYefbR90Ju0MQCdFvt9isyMQ5jxPvJXKzU8fiVHusDsQC9VrtemaOjMMaO9P28pfebsD6oX/pUiQTwutrtxTBNmJOTvp//aGkdn6re1x3DEHiAfla7XRkGzGgUKh/+22jaiD/PYVdwPgg8QL+r3U4iExMwIuo3ccVKHY+WNpTH8St8nx09YLd+HVP6HYovxMKOAYQxgDAGEMYAwhhAGAMIYwBhDCCMAYQxgDAGEMYAwhhAGAMIYwBhDCCMAYQxgDAGEMYAwhhAGAMQERERkYD/AAmIuZw3heC3AAAAAElFTkSuQmCC'
	mainapp.image_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))
	
	data = 'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAADB0lEQVR4nO3dzUtUURjH8d+ZF8PUQCOzoCxoUxNJhdimVWkLk1bSpl0mRNFK7E8YMCIi3Iju2oS0aGEvE+1rMbjSwk3SwoWiQiUyOTNPC1tkmC9zHu/juf4+u8Hxucf7dY4zMnoBIiIiIiIior3EaQ/sam3JOJEeAO0ATgCoAYDMyaPah1Ix8XVmze111rkEYFoEOefccHb0zaTm8dUCdGcyVYXq1GNA7gJI/vvxgAP8rQTB4HzDXN/QUH5F4/gJjSGrJz85Bsh9rHPyYyQJhwcHFxvHensvpjUGqgRY/c7HVY1ZYZD2hsXGRxqTvAN0tbZk/mw7e4qD3Ou/2Xnad453AFeWO4j3tvM/qWS51OM7RGELknb/GaFyHb4T/AM4d9x7RrCk2XeCxg/hWoUZoarzHaDyLIgqxwDGGMAYAxhjAGMMYIwBjDGAMQYwxgDGGMAYAxhjAGOpqA50pftWVIfalomBgTW3t7vO7Ohbr+PzEWCMAYwxgDEGMMYAxhjAGAMYi+x1gIXC8hKmxvNYmJ1BcaW4pc/5MPp8h1e1VmwDFJaX8DH3GsVfBeulbCi2W9DUeH7Xn3wgxgEWZmc2v9MuENsAW93zrcU2QCgYwBgDGGMAYwxgjAGMMYCx2AZIpcP4LUtsA9QfarJewpbENsCpcxeQTldZL2NTsQ2wv+4A2q514vCxZiRTKv9VYEeEsVFWaF91Dc5eurzhffi+oD2OAYwxgDEGMMYAxhjAGAMYi+x1QNTvt6lU1OvkI8AYAxhjAGMMYIwBjDGAMQYwxgDGGMAYAxhjAGMMYIwBjGkE+KEwI1TffQdoBPimMCNQzvtr9w4gcDnfGcES8XtTEBQCJJKJYQAl3zkBKkLKI75DvAO8+jQ+KQ6DvnNCI4Jn2Ze5L75zVJ4FHSmn+wD3XmNWIHILDXMPNQapBBjK51eaJNUJwVMAYfyBbmWKIngyXz93XetCbuqXMrzRdv6MlIq3HVyHrF7KsBYI+kp6PwE3LQ7vyi4xMvBi7HNkiyMiIiIiIiKKnd+mhKZx5r8E9wAAAABJRU5ErkJggg=='
	mainapp.notebook_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))
	
	data = 'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAAE5UlEQVR4nO2c32scVRTHv3cms7O/0mx2bdK0oVTSh7TBqiUUGxCDWBGtiOQvEPUh4JtKwRfbFxFERdQ3q74JvplS0IpQEEWkaYmQ7baFtMQqbZLdZPNjdzY7u9eHZkNnbfbepTM7d3bP5y0752a+e79zzj0zszMAQRAEQRAEQRAEQRAEQRAEQRDtDmt2AP8WIwDeAHACwAEAMVcVcZxhr+G0q/9TYaQN4N8jhAI+BjAJQPdOEjrKBCkDtib/PIDnPNZz3047wwRNKurekd+6yQcAhvf5N+1vgDADtmr+DLwuOzsKaO9MEGcAx5vwa/KBWiZ86Nv+PUZsAMOJFugQaTjVruVIZg3Y77kKGdo0E2TWAO74wDSBRA8QjwGGAWhy67hbXHzrdsPt418MtkjJFtUqULZLKJVmsWmfZi/ePdfM8C7pSMaA/j4g2du0xrZG0wAzZMIMHQUwxX8xZlCojrGX/y1IDZfaCWPA/kGafBm6449jlzHPz+2NyoTLGdDfB8TcveLQ1kQiKUS032RCxWvAdybH0KMPL6rT4BxYzp5kLyydbxQmzoDehGuaOgrGACN8RhQmXoRjUqWsZSjXBTXCDI2IQsQZYBiuaOlIjC5TFCI2oMV9flvBNOEaS7PrM+Iu6M9hLoohdoYdyzScY8oAn5G/FKEIgeqCJKAM8BkywGfIAJ+hLshjqAtSHOqCfIYywGfIAJ8hA3yGuiCPoS5IcQLVBVVKHL++/U/DmKc/2Qs9FJzjKjhKAZQ3KsIYe6PaAiXuESgDSiviybWWyQDPWJvfFMas/y2OUYlgGXBLPLmrN8kAT+AVjuysJYzLpi1U7eB0zoExYPlaCXZRXN/tQhUrN0otUOQOgTFgaaboSazfBMIAzoGlv8Tlp8bSjAUekCoUCANWrlnYXBOfA9TYXKtg5bq8YX4SCAMWpqWedXCOuRSMMqS8AdUyx+JM80fz4pVCILoh5a8F5a5asAvO7sdM6Dg4kUDycHg7Zu6HPIqL9naMbXHk0hYeORJpqd5mUT4Dcmnn0W8mdIy+14/dT0agmwy6ybD7iQiOvtsHs0dvOFZFlDcgP+c8sz04kYAR/b9sI6phaML5MEn9WBVR3oBSznb8XSs7DyJ5yLmtfqyKKG9AfT/fTH8fhHMB5Q0IJ519wnJm57pevy2cUr7HUN+A3rqycnMqj/IDbrqUC1XMTeUdn9WXJBVR3oCBsSjYfbe1Cws2Ln1wFwuXi7AtDtviWLxSxOWPFhxtKNMYBo6r/2yz8jka22Ng3zNx3L64vv1ZKV9B+utsw3H7xuOI7lH+66mfAQAw9GoPeofly0lyOIyhV3Z5qMg9AmEA0xmOTKYwOB5v+OAh0xgGn+3GY5MpML3pF0L6QuB+mLVxp4w7vxeQy1iwsvdqfjjVheShMAbGYoj2q1V2RD/MkjFgFUC3a4o6i1V2LNPTKECmBM27JKYTEc6dzEv7LrgipTP5URQgYYD+FQD521FEDRta9awoSGgAe2o2DeBLVyR1Ehyfs9HrGVGYXBuqxd4B8PPDauoYGC5Aj52SCZUygI1Ol6HFXgLYZwDUv8brHzY4PgWLnWSj02WZAc2/vv6PkcPQK6+D43lwHABDvHmdbQTHOhhuAfgJlcpZdvzGVb8lEQRBEARBEARBEARBEARBEAShFv8BV+didhDwooUAAAAASUVORK5CYII='
	mainapp.zip_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))
	
	data = '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'
	mainapp.rar_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))
	
	data = 'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QA/wD/AP+gvaeTAAACt0lEQVR4nO3c32tScRzG8eeoK12btq01EFKYhCOk0XCnH7J5O+jKvyCii4gVFf0//QtdrXYR0egHVDcFQcam1ixbtDaWK2d6PF3EWbRmzlI/53t8XrfjwOPefDc9yAGIiIiIiIiIiIiIiMjptHo/SKbmzE4OcbqFW2d3/V27Oj2EfscAwhhAmKfZC+r9LbM0+t/R7dfvxBMgjAGEMYAwBhDGAMIYQBgDCOO9oA7hvSCbYgBhDCCMAYQxgDAGEMYAwpQJcPxcHPv9XukZLadMgKGxw9CvTSGoh/7y8VE9ygQAAI+vB9FUDOPnJ+EN+KTntIRSASyDR4eh35hGOBmBpql9HJQMAADuHjdGZ6I4cfEUeof7pOf8M2UDWALhAcSvJH6eBpd6p0H5AMCv0xCfTaA/GJCe0xRHBLD0Bf2YmD2D0ZkoXB41XpoaK5vgcmkIJyOIX07Af+Sg9JyGHBfAcmCkHxOXTiOaisG9zy09py7HBgAATdMQ1EOYvDqFgciQ9JxdOTqAxTfYi/ELJxFNxeDxNv1tzLbqigAAoGlAUA9Bvz6NQ8dGpOds65oAFqNs2OrTs73OYxtVvn5H/kEO+Yc51Iya9Jxtjg9gVAy8e/wGy/czqG5Vpef8wbEBTNPEx+cFZO+kUS6WpefU5cgA60urWJp7hc2VovSUhhwVoPh+A5nbaaxnP0tP2TNHBNjaKOHtvQw+PMvDNNX6RqXSASqlCvILWeQf5VCr2uedTTOUDFAzaig8WUbu7iKqpYr0nP+iVADTNPHp5Qqy869RWvsmPacllAmwtriKzHwam4Uv0lNaSpkAL24+lZ7QFl13L8huGEAYAwhjAGEMIIwBhDGAMD4vqMPX78QTIIwBhDGAMAYQxgDCGEAYAwjj84I6hM8LsikGEMYAREREREREREREREREbfYDH7WyoUqRRoQAAAAASUVORK5CYII='
	mainapp.video_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))
	
	data = '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'
	mainapp.audio_icon2 = ImageTk.PhotoImage(decode_base64_image(size, data))

	data = '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'

	search_size = 16, 16
	mainapp.search_icon2 = ImageTk.PhotoImage(decode_base64_image(search_size, data))

def decode_base64_image(size, data):

	msg = base64.b64decode(data)
	buf = io.BytesIO(msg)
	
	i = Image.open(buf)
	i.thumbnail(size, Image.ANTIALIAS)
	return i