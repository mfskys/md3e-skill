# Adding Motion Physics with Jetpack Compose

> 来源: https://m3.material.io/blog/m3-expressive-motion-theming
> 抓取: 2026-10-19

---

Supercharge your Android transitions and animations with the new M3 Expressive motion theming system.

![Rebecca Franks , Developer Relations Engineer, Android](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fn3jj-rebecca.png?alt=media)

![Austin Fisher , Sr. UX Content Designer](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4foytq-austin.png?alt=media)

![Gus Sonoda , Sr. Staff Motion Designer](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fq3pk-Gus.jpg?alt=media)

Material Design has an exciting new preview release — [Material 3 Expressive](https://m3.material.io/blog/building-with-m3-expressive?utm_source=blog&utm_medium=referral&utm_campaign=IO25). In this latest version 1.4.0-alpha14 of Material 3, you get access to a new theming system: motion!

Previously, Material motion was defined through non-customizable easing and duration values. Today, we’re introducing a new, customizable motion scheme using motion physics defined through a set of motion properties. These can be customized or overridden as needed, giving you more control than ever over how motion works and feels in your product.

Read on to learn how the new motion physics scheme works, how existing APIs have changed, and how to get started.

[▶ Video](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fuzya-Motion_Physics_16-9-aspect.mp4?alt=media)

## Why Material motion?

As a product developer, you know that motion can significantly enhance the user experience. But achieving consistent motion across a complex app can be challenging. The new Material motion system solves this with:

- **Centralized control:** Define your motion theme once, and all Material Components and even your own custom components will inherit it, creating a unified and polished experience, eliminating scattered animation specs.

- **Simplified theming:** Stop fussing with individual duration or easing values. Choose from predefined schemes or create your own, using physics-based spring animations for a natural and engaging feel.

- **Adaptive animations:** Ensure that movement feels fast in the context of the device and adjusts based on user input since animations are not based on predefined time sets.

![Adding Motion Physics with Jetpack Compose](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fyuj5-test.gif?alt=media)

## Getting setup

First, make sure you’re using the latest version of Compose Material 3:

```
androidx.compose.material3:material3:1.4.0-alpha11
```

If you do nothing more than update the Compose dependency, your apps will benefit from applying the standard motion scheme to all your uses of Material Components. But if you do want that extra bit of control, you can customize your scheme to suit your app.

*Note: When 1.4.0 goes to stable, the Material Expressive APIs will move to the next alpha (1.5.0-alphaX), and will no longer be available in 1.4.0. The APIs will go stable in the 1.5.0 release.*

## Fundamentals of the motion system

### Motion schemes: Expressive or Standard

The physics system has two preset motion schemes: **Expressive** and **Standard**. The scheme you choose will define how your product feels. While most motion in a product should use the same scheme, advanced customizations allow you to swap the scheme to emphasize key moments.

- **Expressive** is Material’s recommended motion scheme, and should be used for most situations, particularly hero moments and key interactions.

- **Standard,** with its small amount of bounce, feels more functional and should be used for utilitarian products.

[▶ Expressive: The Expressive motion scheme overshoots the final values to add bounce.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4g88ne-Scheme_Spring_Expressive_Export.mp4?alt=media)

[▶ Standard: The Standard motion scheme eases into the final values.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4g8yey-Scheme_Spring_Standard_Export.mp4?alt=media)

## Animation specs: Spatial or Effect

Two distinct kinds of specifications make up the motion scheme: **Spatial** animation specs and **Effect** animation specs.

**Spatial** specs are used to animate changes in an object's position, orientation, size, and shape. The spring overshoots the final value and bounces into place.

![Spatial springs applied to movement.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4ge2fd-unnamed1.gif?alt=media)

![Spatial springs applied to rotation.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4gf1n5-unnamed2.gif?alt=media)

**Effect** specs are used to animate an object’s properties such as color and opacity, where there shouldn’t be any overshoot.

![Effects springs applied to opacity.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4ghub6-unnamed3.gif?alt=media)

![Effects springs applied to color.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4gjeks-unnamed4.gif?alt=media)

Each animation can also have one of three speeds: **default**, **fast**, and **slow**. Most motion should use the default speed, but smaller elements may benefit from the fast speed and larger elements from the slow.

| Speed | Spatial example | Effects example |
| --- | --- | --- |
| Default | Animations that partially cover the screen, such as [bottom sheets](https://m3.material.io/m3/pages/bottom-sheets/overview) or [expanded navigation rails](https://m3.material.io/m3/pages/navigation-rail/overview) | Opacity of the content within a navigation rail |
| Fast | Animations for small components such as [switches](https://m3.material.io/m3/pages/switch/overview) and [buttons](https://m3.material.io/m3/pages/common-buttons/overview) | Color change of the switch handle |
| Slow | Full-screen [animations](https://m3.material.io/m3/pages/motion-transitions/transition-patterns/) | Full-screen content refresh |

**Speed tokens work across devices.** For example, the **Spatial “fast”** token will always be faster than **“default”** or **“slow,”** but the exact values of each token will differ depending on whether the device is a wearable, phone, or tablet. This ensures the movement feels fast in the context of the device. This also applies when using spring tokens in a custom motion scheme.

[▶ Effects motion in fast, default, and slow speeds](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hb41v-AllSpeeds_Standard_Export.mp4?alt=media)

[▶ Spatial motion in fast, default, and slow speeds](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hc9vj-AllSpeeds_Expressive_Export.mp4?alt=media)

Notice that the Expressive and Standard schemes are presets of opinionated motion values. This makes it easier to swap schemes without changing the underlying property names.

![Expressive and Standard MotionScheme](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hf2tf-unnamed5.png?alt=media)

## Why use motion springs?

If you look at the predefined specifications on the motion schemes, you may notice that springs are used for the backing specifications. Why is this? Spring animations appear more natural by allowing for the ability to interrupt and retarget the animation when required.

For example, consider the difference between using tween and springs:

[▶ Tween interruptions.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hkmsg-00_compare_tween.mp4?alt=media)

[▶ Spring interruptions.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hqa7d-00_compare_spring.mp4?alt=media)

When interrupted and retargeted to a new destination, the spring animation uses its current velocity to perform a more seamless transition between the two states than tween.

It’s also beneficial to use springs to ensure your animations easily **adapt to different screen sizes**, as the tokens will always be slow or fast in the context of the device since it is not time that is specified but rather damping and stiffness. For more details on the benefits of springs, check out the [documentation](https://developer.android.com/develop/ui/compose/animation/customize?_gl=1*9ewdxh*_ga*MzI1NjMyOTExLjE3NjI0MTE3NDU.*_ga_QPQ2NRV856*czE3NzQzNDgyNDgkbzE3OCRnMCR0MTc3NDM0ODM1MCRqNjAkbDAkaDA.#spring?utm_source=blog&utm_medium=motion&utm_campaign=IO25).

## Customizing your motion scheme

The real power of the new system lies in its flexibility. You can tailor the motion scheme to reflect your app’s brand or to underscore an important interaction.

### Choosing between Standard and Expressive schemes

Most developers won’t want to change much in terms of motion theming, but there are two out-of-the-box options for you to choose from: Standard or Expressive. Choosing MaterialExpressiveTheme at the top level will default to the Expressive motion scheme.

Make this choice once for your application at the theme level, and any Material Components with movement built in will use the selected spec from the theme.

```
@Composable
fun YourCustomTheme(){
   MaterialExpressiveTheme(
      motionScheme = MotionScheme.expressive(), // or MotionScheme.standard() 
   ) {

   }
}
```

With the expressive() scheme your apps take on the Material-recommended motion scheme, whereas with the standard(), the motion is, well, pretty standard — there is a minimal amount of bounce, even as both use springs under the hood.

### Creating your own Motion scheme

For more fine-grained control, you can create your own MotionScheme object and return a different AnimationSpec for each property.

In the code snippet below, we create a whole new playfulMotionScheme that by default adds a lot of bounce to components. This demonstrates how you can customize your MotionScheme.

```
@ExperimentalMaterial3ExpressiveApi
fun playfulMotionScheme(): MotionScheme =
    object : MotionScheme {

        override fun <T> defaultEffectsSpec(): FiniteAnimationSpec<T> {
            return spring(
                dampingRatio = Spring.DampingRatioNoBouncy,
                stiffness = 1600f
            )
        }

        override fun <T> defaultSpatialSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = 0.6f, stiffness = 700f)
        }

        override fun <T> fastEffectsSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = Spring.DampingRatioNoBouncy, stiffness = 3800f)
        }

        override fun <T> fastSpatialSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = 0.6f, stiffness = 1400f)
        }

        override fun <T> slowEffectsSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = Spring.DampingRatioNoBouncy, stiffness = 800f)
        }

        override fun <T> slowSpatialSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = 0.6f, stiffness = 300f)
        }
    }

// To use the scheme: In your top level composable

@Composable
fun MyCustomTheme(
    //... other theme properties
    content: @Composable () -> Unit
) {
    MaterialExpressiveTheme(
        //.... other theme properties
        motionScheme = playfulMotionScheme(),
        content = {
            content()
        }
    )
}
```

[▶ FAB menu with an extra-stiff custom scheme.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4lh9wb-Customization_Fab_Instant_Export.mp4?alt=media)

[▶ FAB menu with very low stiffness custom scheme.](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4ligvz-Customization_Fab_Soft_Export.mp4?alt=media)

## Custom component animations

To maintain consistency with other Material Components, ensure your custom components adopt the recommended motion changes and use the motion specs available through MaterialTheme.motionScheme.

For example, the following code uses tween() calls to animate the size and color of a text component when pressing and releasing its container:

```
val interactionSource = remember { MutableInteractionSource() }
val isPressed by interactionSource.collectIsPressedAsState()
val scale by
  animateFloatAsState(
      targetValue = if (isPressed) 8f else 1f,
      animationSpec = tween(1000),
      label = "scale"
  )
val color by
  animateColorAsState(
      targetValue = if (isPressed) Color.Green else Color.Red,
      animationSpec = tween(1000),
      label = "color"
  )
Box(
  modifier =
      Modifier.fillMaxSize().clickable(
          interactionSource = interactionSource,
          indication = null
      ) {}
) {
  Text(
      text = "Hello",
      modifier =
          Modifier.graphicsLayer {
                  scaleX = scale
                  scaleY = scale
                  transformOrigin = TransformOrigin.Center
              }
              .align(Alignment.Center),
      style = LocalTextStyle.current.copy(color = color, textMotion = TextMotion.Animated)
  )
}
```

Since scale represents a Spatial motion and color falls under Effects motion, we can leverage the motion scheme for consistent application. This approach aligns your component’s motion to the overall app experience and allows it to adapt automatically when switching between Standard and Expressive schemes/themes.

```
val interactionSource = remember { MutableInteractionSource() }
val isPressed by interactionSource.collectIsPressedAsState()
val scale by
  animateFloatAsState(
      targetValue = if (isPressed) 8f else 1f,
      animationSpec = MaterialTheme.motionScheme.defaultSpatialSpec<Float>(),
      label = "scale"
  )
val color by
  animateColorAsState(
      targetValue = if (isPressed) Color.Green else Color.Red,
      animationSpec = MaterialTheme.motionScheme.defaultEffectsSpec<Color>(),
      label = "color"
  )
Box(
  modifier =
      Modifier.fillMaxSize().clickable(
          interactionSource = interactionSource,
          indication = null
      ) {}
) {
  Text(
      text = "Hello",
      modifier =
          Modifier.graphicsLayer {
                  scaleX = scale
                  scaleY = scale
                  transformOrigin = TransformOrigin.Center
              }
              .align(Alignment.Center),
      style = LocalTextStyle.current.copy(color = color, textMotion = TextMotion.Animated)
  )
}
```

## Individual Material Component changes

In the expressive update, most Material 3 components use the motion physics system by default.

To add the motion-physics system to other components, including those that are custom built, use the specifications from above. See the full [M3 Expressive announcement blog post](https://m3.material.io/blog/building-with-m3-expressive?utm_source=blog&utm_medium=motion&utm_campaign=IO25) for more details on the new components.

## Get started today

Try out the new motion subsystem in Material 3 Expressive today, and let us know how you like it by tagging us on social media @GoogleDesign. If you find any issues, please file them on the [issue tracker](https://b.corp.google.com/issues/new?component=742043&template=1590761?utm_source=blog&utm_medium=referral&utm_campaign=IO25).

Happy theming!

*Special thanks to Material motion designers Gus Winkelman and Gustavo Gonzalez.*

## Up next

[![Adding Motion Physics with Jetpack Compose](https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4mdykz-unnamed6.png?alt=media)](https://m3.material.io/blog/building-with-m3-expressive)
