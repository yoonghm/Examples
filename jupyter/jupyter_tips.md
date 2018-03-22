# Jupyter Notebook Tips

## Start Jupyter Notebook via Command Line

<pre>
$ <b>jupyter notebook</b>
</pre>

## Changing Default Indentation to 2 Spaces

Enter the following snippet in the browser's JavaScript console once.

```JavaScript
var cell = Jupyter.notebook.get_selected_cell();
var config = cell.config;
var patch = {
      CodeCell:{
        cm_config:{indentUnit:2}
      }
    }
config.update(patch)
```

Then reload the notebook. This setting is persistent.

## Restore Default (4 Spaces) Indentation

Enter the following snippet in the browser's JavaScript console once:

```JavaScript
var cell = Jupyter.notebook.get_selected_cell();
var config = cell.config;
var patch = {
      CodeCell:{
        cm_config:{indentUnit: null} // only change here.
      }
    }
config.update(patch)
```
