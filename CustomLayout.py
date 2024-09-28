import sublime
import sublime_plugin

class SetCustomLayoutCommand(sublime_plugin.EventListener):
    def on_post_window_command(self, window, command, args):
        """
        # "cols" is an array of values between 0 and 1 that represent the proportional position of each column break
        # "rows" is the same as cols
        # "cells" is an array of arrays, each inner array contains [x1, y1, x2, y2] coordinates of the cell
        # Further details: https://forum.sublimetext.com/t/set-layout-reference/5713

        Example:
            layout = {
                "cols": [0.0, 0.5, 1.0],
                "rows": [0.0, 0.25, 0.75, 1.0],
                "cells": [
                    [0, 0, 1, 2], [1, 0, 2, 1],
                    [0, 2, 1, 3], [1, 1, 2, 3]
                ]
            }
            window.set_layout(layout)

        Diagram of the example code:

                 0,0                            1,0                             2,0
        0.0 +    +-------------------------------+-----------------------------+
            |    | (a.file)                      | (b.file)                    |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            v    |                              1,1                           2,1
        0.25+    |                               +-----------------------------+
            |    |                               | (c.file)                    |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |  0,2                              1,2                            |
            v    +-------------------------------+                             |
        0.75+    | (d.file)                      |                             |
            |    |                               |                             |
            |    |                               |                             |
            v   0,3                             1,3                           2,3
        1.0 +    +-------------------------------+-----------------------------+

        """

        layout = {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells": [[0, 0, 1, 2], [1, 0, 2, 1], [1, 1, 2, 2]]
        }
        window.set_layout(layout)


        """
        Visualization of layout generated from code above:

                0,0                             1,0                           2,0
        0.0 +    +-------------------------------+-----------------------------+
            |    | (main.cpp)                    | (inputf.in)                 |
            |    |                               | 2                           |
            |    | #include <bits/stdc++.h>      | 1 2 3                       |
            |    | using namespace std;          | 219 8219 483                |
            |    |                               | 8 5 5                       |
            |    | int main() {                  | 12 123 83 820 930           |
            |    |     ios::sync_with_stdio(0);  |                             |
            |    |     cin.tie(0);               |                             |
            |    |     cout.tie(0);              |                             |
            |    |                               |                             |
            v    |     int t; cin >> t;         1,1                           2,1
        0.5 +    |     while (t--) {             +-----------------------------+
            |    |                               | (outputf.out)               |
            |    |     }                         | 12 8                        |
            |    |     return 0;                 | 6 9                         |
            |    | }                             |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            |    |                               |                             |
            v   0,2                             1,2                           2,2
        1.0 +    +-------------------------------+-----------------------------+
        """
