# JS Prefer Objects

> Sublime Text plugin coming soon 🤗

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
