# Sublime objectify

> 🚧 This was thrown together to learn more about sublime plugins and is not fully working

Change your switch statements...

```js
switch (isFruit) {
    case "pitaya":
        return true;
        break;
    case "mango":
        return true;
        break;
    case "spinach":
        return false;
        break;
    default:
        return false;
}
```

...to object literals, woo!

```js
const isFruit = type =>
    ({
        pitaya: true,
        mango: true,
        spinach: false,
        default: false
    }[type || "default"]);
```

## Contributing

We'd love your help improving this little tool!

* Move `js-prefer-objects.py` to your Sublime Text user plugins folder
* Open ST console (`` ctrl+` ``)
* Run the command: `view.run_command("js_prefer_objects")`
