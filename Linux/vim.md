# Vi or Vim

## Brief Overview of vi/vim

vi, stands for **vi**sual editor, is the De facto full-screen text editor came with every distribution of Unix and Linux operating systems.

vim, stands for **v**sual editor *im*prove, is a variant that offer better features than the original vi editor. It is distributed in all modern Unix and Linux operating systems.

The first editor available to Unix is **ed** which allowed user to view and edit one line of text a time.  Hence vi/vim, full-screen text editor, was a consider a visual editor at that time.

## Usage

Text-based vi/vim editor does not provide menu items nor toolbar icons to interact with user. These editors offer 3 modes to accept inputs from users

- **Command mode**
  User can enter into command mode by pressing one or more *ESC* key.<br />
  Any input is considered as command. 
  
- **Edit mode**
  User can enter into edit mode by pressing <br />
  *i*   - **i**nsert before cursor<br />
  *a*   - **a**pend after cursor<br />
  *I*   - **I**nsert at the beginning of current line<br />
  *A*   - **A**pend after the end of current line<br />
  *o*   - **o**pen a new line below current line<br />
  *O*   - **O**pen a new line above current line<br />
  *r*   - **r**place current character with the next input input character<br />
  *R*   - **R**place current characters onwards with the next input characters<br />
  *c*M  - **c**hange character in the M-direction with the next input character<br />
          M could be<br />
            *^* (beginning of current line)<br />
            *$* (end of current line)<br />
                    
  *C
