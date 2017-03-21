# import the gtk library
import gtk

# create the application or class
class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()
        
        # set the titile name
        self.set_title('incf_buttons_test')
        # set the size of the window 400 x 300
        self.set_size_request(400, 300)
        # set the position with is the window center
        self.set_position(gtk.WIN_POS_CENTER)
        # starting the actual codes
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
        # finished the program by clicking quit button
        self.connect('destroy', gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()
