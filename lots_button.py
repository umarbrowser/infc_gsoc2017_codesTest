import gtk

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title('janyo kasa')
        self.set_size_request(400, 300)
        self.set_position(gtk.WIN_POS_CENTER)
        sw = gtk.ScrolledWindow()
        table = gtk.Table(10, 10)
        table.set_row_spacings(10)
        table.set_col_spacings(10)
        for i in range(1, 11):
            for j in range(1, 11):
                caption = 'Mdn' + str(j) + str(i)
                btn = gtk.Button(caption)
                table.attach(btn, i, i+1, j, j+1)
        sw.add_with_viewport(table)
        self.add(sw)

        self.connect('destroy', gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()