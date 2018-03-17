# vim Editor

## Brief Overview of vim

**vim** is the **im**proved version of **vi**. **vi** stands for **vi**sual editor, is the De facto full-screen text editor came with every distribution of Unix and Linux operating systems.

vim offers better features than the original vi editor. It is distributed in all modern Unix and Linux operating systems.

The first editor available to Unix is **ed** which allowed user to view and edit one line of text a time.  Hence vi/vim, full-screen text editor, was a consider a visual editor at that time.

## Usage

Text-based vi/vim editor does not provide menu items nor toolbar icons to interact with user. These editors offer 3 modes to accept inputs from users

1. **Command mode**
    - Users enter document-editing commands to vi/vim editor
    - Users enter this mode by hitting one or more *ESC* key

2. **Edit mode**
    - Users enter this mode by using one of the edit command as shown in the [edit mode table](#edit-mode).
    - Users edit their documents in this mode

3. **Ex mode**
    - Users enter this mode by entering "**:**"
    - User could enter extensive command to vi/vim editor

## Command Mode

| **Command**   | **Description**                                        |
|:-------------:|:-------------------------------------------------------|
| **h**         | Move cursor to the left                                |
| **l**         | Move cursor to the right                               |
| **j**         | move cursor to the down                                |
| **k**         | Move cursor to the up                                  |
| **b**         | Move cursor to the beginning of the word on the left   |
| **w**         | Move cursor to the end of the word on the right        |
| **{**         | Move cursor to the beginning of the previous paragraph |
| **}**         | Move cursor to the end of the previous paragraph       |
| **M**         | Move cursor to the middle line of window               |
| *n***H**      | Move cursor to the *n* lines from **H**ead             |
| *n***L**      | Move cursor to the *n* lines form **B**ottom           |
| *n*<b>\|</b>  | Move cursor to column *n* of current line              |
| *n***G**      | Move cursor to line *n*, default the last line         |
| *n*<b>%</b>   | Move cursor to percentage *n* of the file              |
| **^**         | Move cursor to the beginning of current line           |
| **$**         | Move cursor to the end of current line                 |
| **dd**        | Delete current line                                    |
| *n***d**      | Delete *n* line below current line                     |

## Edit Mode

| **Command**   | **Description**                                        |
|:-------------:|:-------------------------------------------------------|
| **i**         | **i**nsert before cursor                               |
| **a**         | **a**pend after cursor                                 |
| **I**         | **I**nsert at the beginning of current line            |
| **A**         | **A**pend after the end of current line                |
| **o**         | **o**pen a new line below current line                 |
| **O**         | **O**pen a new line above current line                 |
| **r**         | **r**eplace current character with next input          |
| **R**         | **R**eplace current character onwards with next input  |
| *c*M          | **c**hange character in the M-direction with next input<br />M could be<br />*^* (beginning of current line)<br />*$* (end of current line)<br />|
| *C*           | Change to the end of line                              |

## Ex Mode

| **Command**   | **Description**                                        |
|:-------------:|:-------------------------------------------------------|
| **:w**        | Save file (aka edit buffer)                            |
| **:q!**       | Discard changes to the file and exit                   |
| **:e!**       | Revert to content stored in the file                   |
| **:wq**       | Save file (file name is supplied during open)and quit  |
| **:wq** *name*| Save file to *name* to disk and quit                   |
| **:w** *name* | Save file to *name* to disk                            |


