import datetime, getpass
import sublime, sublime_plugin
class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s %s" %( datetime.date.today().strftime("%Y/%m/%d"), datetime.datetime.now().strftime("%H:%M")) } )