# vim Editor

## Brief Overview of vim

**vim** is the **im**proved version of **vi**. **vi** stands for **vi**sual editor, is the De facto full-screen text editor came with every distribution of Unix and Linux operating systems.

vim offers better features than the original vi. It is distributed in all modern Unix and Linux operating systems.

The first editor available to Unix is **ex** which allowed user to view and edit one line of text a time.  Hence vi/vim, full-screen text editor, was a consider a visual editor at that time.

## Usage

```
vi
```
Start vi/vim by enter

```
vi file1 file2
```
Edit one or more files by providing the file names, separated by one or more spaces to `vi`

```
vi -R file
```
Open file for reading only

```
vi +n file
```
Open file at line number *n*

## Various Modes Available in vi/vim

Text-based vi/vim does not provide menu items nor toolbar icons to interact with user.

vi commands are case sensitive.

These editors offer 3 modes to accept inputs from users:

1. **Command mode**
    - Users enter this mode by hitting one or more *ESC* key
    - Users enter document-editing commands to vi/vim
    - These commands are accepted by vi/vim without *ENTER*

2. **Edit mode**
    - Users enter this mode by using any one of the edit commands as shown in the [edit mode table](#edit-mode)

3. **Ex mode**
    - Users enter this mode by entering "**:**", "**/**" or "**?**"
    - User could enter extensive command to vi/vim
    - These commands are only accepted by vi/vim if they are followed by *ENTER*

### Command Mode

| **Command**   | **Description**                                        |
|:-------------:|:-------------------------------------------------------|
| **0**         | Move to beginning of current line                      |
| *n***h**      | Move left *n* times                                    |
| *n***l**      | Move right *n* times                                   |
| *n***j**      | Move down *n* times                                    |
| *n***k**      | Move up *n* times                                      |
| *n***b**      | Move to **b**eginning of current or previous *n* word(s)|
| *n***B**      | Move to **b**eginning of current or previous *n* word(s), ignoring punctuation|
| *n***e**      | Move to **e**nd of current or next *n* word(s)         |
| *n***E**      | Move to **e**nd of current or next *n* word(s), ignoring punctuation|
| *n***w**      | Move to beginning of next *n* **w**ord(s)              |
| *n***W**      | Move to beginning of next *n* **w**ord(s), ignoring punctuation|
| **(**         | Move to beginning of current sentence                  |
| **)**         | Move to beginning of next sentence                     |
| **{**         | Move to beginning of previous paragraph                |
| **}**         | Move to end of previous paragraph                      |
| **[[**        | Move to beginning of previous section                  |
| **]]**        | Move to end of previous section                        |
| *n***H**      | Move to *n* lines below top line of the screen         |
| **M**         | Move to middle line of screen                          |
| *n***L**      | Move to *n* lines above last line of the screen        |
| *n*<b>\|</b>  | Move to *n* character of current line                  |
| *ENTER*       | Move to first character of next line                   |
| **++**        | Move to first character of next line                   |
| **-**         | Move to first character of prvious line                |
| **^**         | Move to first nonblank character of current line       |
| *n***G**      | Move to line *n*, default the last line                |
| *n*<b>%</b>   | Move to percentage *n* of the file                     |
| **^**         | Move to beginning of current line                      |
| **$**         | Move to end of current line                            |
| **x**         | Delete current character                               |
| **dd**        | Delete current line                                    |
| **dw**        | Delete from currect character to end of word           |
| **d$**        | Delete to end of current line                          |
| *n***dd**     | Delete *n* lines from current line downward            |
| **D**         | Delete from current character to end of current line   |
| **u**         | Undo *previous* change                                 |
| **yy**        | Yank current line                                      |
| *n***yy**     | Yank *n* lines from current line downward              |
| **y$**        | Yank from currect character to end of current line     |
| **p**         | Paste after current cursor                             |
| **P**         | Paste before current cursor                            |
| **m***a*      | Mark current position as *a*                           |
| **marks**     | Display active bookmarks                               |
| **''**        | Return to beginning of previous mark or context        |
| **\`\`**      | Return to exact position of previous mark or context   |
| <b>\`</b>*x*  | Jump to bookmark *x*                                   |
| <b>y\`</b>*x* | Yank text until bookmark *x*                           |
| <b>d\`</b>*x* | Delete from current character toward bookmark *x*      |
| **ZZ**        | Save changes and exit                                  |
| **~**         | Toggle case of current character and forward cursor    |
| **J**         | Join current line with next line                       |
| **.**         | Repeat the last command                                |
| *CTRL*+**F**  | Scroll forward one screen                              |
| *CTRL*+**B**  | Scroll backward one screen                             |
| *CTRL*+**D**  | Scroll forward half screen                             |
| *CTRL*+**U**  | Scroll backward half screen                            |
| *CTRL*+**E**  | Scroll forward one line                                |
| *CTRL*+**Y**  | Scroll backward one line                               |
| **z**+*ENTER* | Move current line to top of screen and scroll          |
| **z.**        | Move current line to center of screen and scroll       |
| **z-**        | Move current line to bottom of screen and scroll       |
| *CTRL*+**L**  | Redraw the screen                                      |
| *CTRL*+**G**  | Display line number, total number of lines, etc        |

### Edit Mode

| **Command**   | **Description**                                        |
|:-------------:|:-------------------------------------------------------|
| **i**         | Insert before cursor                                   |
| **a**         | Append after cursor                                    |
| **I**         | Insert at the beginning of current line                |
| **A**         | Apend after the end of current line                    |
| **o**         | Open a new line below current line                     |
| **O**         | Open a new line above current line                     |
| **r**         | Replace current character                              |
| **R**         | Replace current line from current character            |
| **c***M*      | Change character in the *M*-direction with next input<br />*M* could be<br />*^* (beginning of current line)<br />*$* (end of current line)<br />|
| **cw**        | Change current word from current character             |
| **cc**        | Change current line                                    |
| **C**         | Change current line from current character             |
| **s**         | Delete current character and substitute text           |
| **S**         | Change entire line                                     |
| **n**         | Repeat search in the same direction                    |
| **N**         | Repeat search in opposite direction                    |

### Ex Mode

| **Command**   | **Description**                                        |
|:-------------:|:-------------------------------------------------------|
| **:w**        | Save file                                              |
| **:w!**       | Save to the existing file                              |
| **:w** *name* | Save to file *name*                                    |
| **:q!**       | Discard changes to the file and exit                   |
| **:e**        | Reopen the file                                        |
| **:e!**       | Discard changes and reopen the file                    |
| **:wq**       | Save file (file name is supplied during open)and quit  |
| **:wq** *name*| Save a copy of file to *name* and quit                 |
| **:w** *name* | Save a copy to of file to *name*                       |
| **:o** *name* | Open file *name*                                       |
| **:rew**      | Open previous file                                     |
| **:n**        | Open next file given in argument to vi/vim             |
| **:!***cmd*   | Execute shell command *cmd*                            |
| **:r**        | Append content of current file                         |
| **:r** *!cmd* | Append the output from shell command *cmd*             |
| <b>/</b>*pattern* | Search *pattern*                                   |
| <b>?</b>*pattern* | Search backward for *pattern*                      |


## Search and Replace Examples

```
:s/foo/bar/g
```
Search and replace *each* occurence of 'foo' to 'bar' in current line.

```
:%s/foo/bar/
```
In all lines, search and replace *first* occurence of 'foo' to 'bar'.

```
:%s/foo/bar/g
```
In all lines, search and replace *each* occurence of 'foo' to 'bar'.

```
:%s/foo/bar/gc
```
In all lines, search and replace *each* occurence of 'foo' to 'bar',but ask for confirmation in each case.

```
:%s/foo/bar/gci
```
In all lines, search by ignoring case sensitive, and replace *each* occurence of 'foo' to 'bar', but ask for confirmation in each case.<br />
`:%s/foor\c/bar/gc` has the same effect.<br />
Alternatively use `:set ignorecase` before running the command `%s/foo/bar/gc`.

```
:%s/foo/bar/gcI
```
In all lines, search by case sensitive, and replace *each* occurence of 'foo' to 'bar', but ask for confirmation in each case.<br />
`:%s/foor\C/bar/gc` has the same effect.<br />
Alternatively use `:set noignorecase` before running the command `%s/foo/bar/gc`.

```
:5,12s/foo/bar/g
```
Search and replace *each* occurence of 'foo' to 'bar' from line 5 to line 12 (inclusive).

```
:`a,`bs/foo/bar/g
```
Search and replace *each* occurence of 'foo' to 'bar' from bookmark *a* to bookmark *b* (inclusive)

```
:.,`bs/foo/bar/g
```
Search and replace *each* occurence of 'foo' to 'bar' from current line to bookmark *b* (inclusive)

```
:.,$s/foo/bar/g
```
Search and replace *each* occurence of 'foo' to 'bar' from current line to the last line (inclusive).
