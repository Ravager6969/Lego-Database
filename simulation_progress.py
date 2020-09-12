class progress(object):
    def __init__(self, message='', message_list=[], repeat=False, repeat_frequency=0, percent=False, percent_length=0, percent_display_length=1):
        self.message = message
        self.repeat = repeat
        self.repeat_frequency = repeat_frequency #how often you want to add a new message
        self.repeat_counter = 0
        self.message_list = message_list
        if message_list != []:
            self.message_list_counter = 0
        if self.repeat == False:
            print(self.message)
        self.percent = percent
        self.percent_length = percent_length
        if self.percent != False:
            self.percent_counter = 1
            self.percent_display_length = percent_display_length
    def add_progress(self):#def add to add to a bar each time so everytime something happens you can add to the bar
        if self.repeat != False:
            if self.repeat_counter == self.repeat_frequency:
                print(self.message,end='')
                self.repeat_counter = 0
            else:
                self.repeat_counter += 1
        elif self.message_list != []:
            print(self.message_list[self.message_list_counter])
            self.message_list_counter += 1
        elif self.percent != False:
            if int(str(('%.'+str(self.percent_display_length)+'f') % (float(self.percent_counter/self.percent_length)*100))) <= 100:
                print(str(('%.'+str(self.percent_display_length)+'f') % (float(self.percent_counter/self.percent_length)*100))+'%'+' '+self.message)
                self.percent_counter += 1
    def finnish_progress(self, finnish_message, time, units='Seconds', time_length=1):
        time = ('%.'+str(time_length)+'f') % time
        print('\n'+finnish_message)
        print(f'Time Elapsed: {time} {units}')
if __name__ == "__main__":
    import time
    import sys
    test = progress('Done', percent=True, percent_length=30, percent_display_length=0)
    test = progress('-', repeat=True, repeat_frequency=100000)
    while True:
        try:
            test.add_progress()
        except KeyboardInterrupt:
            test.finnish_progress('Completed', 10)
            sys.exit()
        #time.sleep(0.5)
        
