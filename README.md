# JS Prefer Objects

> Builds coming soon 🤗

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
* Open ST console (Ctrl+`)
* Run the command: `view.run_command("js_prefer_objects")`
