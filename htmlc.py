#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
import os, sys
from pydebugger.debug import debug
from make_colors import make_colors
import argparse
if sys.version_info.major == 3:
    raw_input = input
from configset import configset
import re

APP_PATH = r'c:\Program Files (x86)\David Esperalta\HtmlCompiler\HtmlCompilerCmd.exe'
sys.path.append(os.path.dirname(APP_PATH))

class HTMLc(object):
    def __init__(self, configname = None):
        self.configname = configname
        self.config = None
        debug(self_configname = self.configname)
        self.real_configname = os.path.join(os.path.dirname(__file__), 'test.hcp')
        if not self.configname:
            self.configname = os.path.join(os.path.dirname(__file__), 'test.hcp')
        debug(self_configname = self.configname)
        if self.configname:
            self.configname = self.format_configname(self.configname)
        if not self.configname:
            self.configname = raw_input(make_colors('config name: ', 'lw', 'lr', ['blink']))
        if not self.configname:
            print(make_colors("Invalid config name !", 'lw', 'lr', ['blink']))
        if self.configname:
            self.config = configset(self.configname)
            
    def random_output(self):
        from datetime import datetime
        str_date = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
        return "HTMLCompiler_" + str_date + ".exe"
    
    def convert_ico(self, image):
        if os.path.splitext(image)[1] == '.ico':
            return image
        try:
            from PIL import Image
        except:
            print(make_colors("No PILLOW/PIL module !", 'lw', 'lr', ['blink']))
            return ''
        img = Image.open(image)
        img.save(os.path.join(os.path.dirname(__file__), 'favicon.ico'), format = 'ICO', sizes = [(32, 32)])
        
        return os.path.join(os.path.dirname(__file__), 'favicon.ico')
        
    def format_configname(self, configname = None):
        if not configname:
            return None
        if not os.path.split(configname)[0]:
            configname = os.path.abspath(configname)
        configname_ext = os.path.splitext(configname)[1]
        configname_name = os.path.basename(os.path.splitext(configname)[0])
        configname_temp = os.path.abspath(configname_name) + "_temp" + configname_ext
        debug(configname = configname)
        with open(configname, 'rb') as f:
            f1 = f.read().decode('utf-16')
            #print("f1 =", f1)
        with open(configname_temp, 'wb') as g:
            g.write(f1)
        return configname_temp
    
    def set_theme(self, theme = None, default = 'Metro Black'):
        all_themes = ['Amakrits', 'Amethyst Kamri', 'Aqua Graphite', 'Aqua Light Slate', 'Auric', 'Blue Graphite', 'Carbon', 'Charcoal Dark Slate', 'Cobalt XEMedia', 'Cyan Dusk', 'Cyan Night', 'Emerald Light Slate', 'Golden Graphite', 'Green Graphite', 'Iceberg Classico', 'khaki', 'Lavender Classico', 'Light Green', 'Lilac', 'Metro Black', 'Metro Blue', 'Metro Green', 'Orange', 'Orange Graphite', 'Pink', 'Ruby Graphite', 'Sapphire Kamri', 'sepia', 'Sky', 'Slate Classico', 'Smokey Quartz Kamri', 'Turquoise Gray', 'Windows', 'Yellow Graphite']
        if not theme:
            n = 1
            for i in all_themes:
                if len(str(n)) == 1:
                    number = '0' + str(n)
                else:
                    number = str(n)                
                print(make_colors(number, 'lc') + ". " + make_colors(i, 'lw', 'bl'))
                n += 1
            qtheme = raw_input("Select theme number: ")
            if str(qtheme).isdigit() and int(qtheme) <= len(all_themes):
                theme = all_themes[int(qtheme) - 1]
            else:
                theme = default
        if not theme:
            theme = default
        return theme
    
    def usage(self):
        parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
        parser.add_argument('-n', '--title', action = 'store', help = 'Title name, default = "HTMLCompiler"', default = "HTMLCompiler")
        parser.add_argument('-t', '--theme', action = 'store', help = 'Theme name, default = "Metro Black"')
        parser.add_argument('-i', '--icon', action = 'store', help = 'Icon path')
        parser.add_argument('-P', '--password', action = 'store', help = 'Password for decompiler')
        parser.add_argument('-f', '--index', action = 'store', help = 'Index File *.htm *.html')
        parser.add_argument('-o', '--output', action = 'store', help = 'Output name with/without ext *.exe, default = "HTMLCompiler_date.exe"')
        parser.add_argument('-e', '--excepts',  action = 'store', help = 'Exception/Exclude file mask')
        parser.add_argument('-B', '--border', action = 'store', help = 'Window border, default = 2', default = 2, type = str)
        parser.add_argument('-W', '--width', action = 'store', help = 'Window Width, default = 800', default = 800, type = str)
        parser.add_argument('-H', '--height', action = 'store', help = 'Window Height, default = 600', default = 600, type = str)
        parser.add_argument('-mW', '--min-width', action = 'store', help = 'Min window width', default = 0, type = str)
        parser.add_argument('-MW', '--max-width', action = 'store', help = 'Max window width', default = 0, type = str)
        parser.add_argument('-mH', '--min-height', action = 'store', help = 'Min window height', default = 0, type = str)
        parser.add_argument('-MH', '--max-height', action = 'store', help = 'Min window height', default = 0, type = str)
        parser.add_argument('-eX', '--extract-ext', action = 'store', help = 'Extract file extention, default = "zip mp3 mp4"', default = "zip mp3 mp4")
        parser.add_argument('-X', '--extention', action = 'store', help = 'Output/Saveas Extention, default = ".exe"', default = "exe")
        parser.add_argument('-tr', '--tray', action = 'store_true', help = 'Enable window icon tray')
        parser.add_argument('-C', '--upx', action = 'store_true', help = 'Compress with APX')
        parser.add_argument('-c', '--compress', action = 'store_true', help = 'Compress Content')
        parser.add_argument('-es', '--escape', action = 'store_true', help = 'Enable Escape Close funtion, press escape/esc key to close window')
        parser.add_argument('-j', '--show-jserror', action = 'store_false', help = 'Show Javascript Error')
        parser.add_argument('-cp', '--enable-copy', action = 'store_true', help = 'Enable copy Text')
        parser.add_argument('-s', '--enable-wstyle', action = 'store_true', help = 'Enable Window Style')
        parser.add_argument('-r', '--enable-worder', action = 'store_true', help = 'Enable Window Order')
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            if not args.index:
                sys.exit(make_colors("No Index file given !", 'lw', 'lr', ['blink']))
            index = args.index
            if not os.path.isfile(args.index):
                sys.exit(make_colors("Invalid Index file !", 'lw', 'lr', ['blink']))            
            if not os.path.split(args.index)[0]:
                index = os.path.abspath(args.index)
            if not args.output:
                args.output = self.random_output()
            if args.tray:
                args.tray = '1'
            else:
                args.tray = '0'
            if args.compress:
                args.compress = '1'
            else:
                args.compress = '0'
            if args.upx:
                args.upx = '1'
            else:
                args.upx = '0'
            if args.escape:
                args.escape = '1'
            else:
                args.escape = '0'
            if args.show_jserror:
                args.show_jserror = '1'
            else:
                args.show_jserror = '0'
            if args.enable_copy:
                args.enable_copy = '1'
            else:
                args.enable_copy = '0'
            if args.enable_wstyle:
                args.enable_wstyle = '1'
            else:
                args.enable_wstyle = '0'
            if args.enable_worder:
                args.enable_worder = '1'
            else:
                args.enable_worder = '0'
            if args.icon:
                args.icon = self.convert_ico(args.icon)
            if not os.path.splitext(args.output)[1]:
                args.ouput = args.output + ".exe"
            self.config.write_config('HtmlCompiler', 'AppTitle', args.title)
            self.config.write_config('HtmlCompiler', 'IndexPage', index)
            self.config.write_config('HtmlCompiler', 'AppPassword', args.password)
            self.config.write_config('HtmlCompiler', 'OutputFile', args.output)
            self.config.write_config('HtmlCompiler', 'ExcludeFileMasks', args.excepts)
            self.config.write_config('HtmlCompiler', 'AppBorderStyle', args.border)
            self.config.write_config('HtmlCompiler', 'AppWindowWidth', args.width)
            self.config.write_config('HtmlCompiler', 'AppWindowHeight', args.height)
            self.config.write_config('HtmlCompiler', 'AppWindowMinWidth', args.min_width)
            self.config.write_config('HtmlCompiler', 'AppWindowMinHeight', args.min_height)
            self.config.write_config('HtmlCompiler', 'AppWindowMaxWidth', args.max_width)
            self.config.write_config('HtmlCompiler', 'AppWindowMaxHeight', args.max_height)
            self.config.write_config('HtmlCompiler', 'ExtractFileExts', args.extract_ext)
            self.config.write_config('HtmlCompiler', 'ExecuteFileExts', args.extention)
            self.config.write_config('HtmlCompiler', 'ExecuteFileExts', args.extention)
            self.config.write_config('HtmlCompiler', 'UseTrayIcon', args.tray)
            self.config.write_config('HtmlCompiler', 'CompressContents', args.compress)
            self.config.write_config('HtmlCompiler', 'AppWindowStyle', args.enable_wstyle)
            self.config.write_config('HtmlCompiler', 'AppWindowOrder', args.enable_worder)
            self.config.write_config('HtmlCompiler', 'AppEscapeClose', args.escape)
            self.config.write_config('HtmlCompiler', 'CompressWithUpx', args.upx)
            self.config.write_config('HtmlCompiler', 'HideJsErrors', args.show_jserror)
            self.config.write_config('HtmlCompiler', 'AllowCopyText', args.enable_copy)
            self.config.write_config('HtmlCompiler', 'IconPath', args.icon)

            args.theme = self.set_theme(args.theme)
            
            self.config.write_config('HtmlCompiler', 'AppTheme', args.theme)
            
            with open(self.configname, 'rb') as f:
                g = f.read()
                g = re.sub(" = ", "=", g)
                g = g.encode('utf-16')
            with open(self.real_configname, 'wb') as f1:
                f1.write(g)
            
            #os.system("type " + self.real_configname)
            os.system("HtmlCompilerCmd.exe " + self.real_configname)
            import subprocess
            subprocess.Popen(args.output)
            
if __name__ == '__main__':
    c = HTMLc()
    c.usage()
    #c.format_configname()
