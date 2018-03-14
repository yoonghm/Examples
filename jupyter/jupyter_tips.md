# Jupyter Tips

## Changing Default's Indentation

Enter the following snippet in the browser's JavaScript console once.

```javascript
var cell = Jupyter.notebook.get_selected_cell();
var config = cell.config;
var patch = {
      CodeCell:{
        cm_config:{indentUnit:2}
      }
    }
config.update(patch)
```

Then reload the notebook. This setting persists until the next run of the snippet.
