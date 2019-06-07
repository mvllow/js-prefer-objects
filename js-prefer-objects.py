import sublime
import sublime_plugin

import re

_switch_regex = r"switch\s*\((?P<switchName>\w*)\)\s\{"
_case_regex = r"(?:[\s\S]*?case\s*\W*(?P<caseName>\w*)\W*?:)(?P<caseContent>[\s\S]*?)break"
_default_regex = r""

class JsPreferObjects(sublime_plugin.TextCommand):
    def run(self, edit):
        bufferText = self.view.substr(sublime.Region(0, self.view.size()))

        switch = re.findall(_switch_regex, bufferText)
        cases = re.findall(_case_regex, bufferText)
        default = re.findall(_default_regex, bufferText)

        content = "const " + switch[0].strip() + " = type =>\n"
        content += "    ({"
        for case in cases:
            content += "\n        \"" + case[0].strip() + "\": " + case[1].replace('return', '').replace(';', ',').strip()
        content += "\n    }[type || 'default']);" 

        self.view.insert(edit, 0, content)
