<template>
  <span
    :style="{ fontSize: `${size}rem` }"
    :class="classes"
    :aria-hidden="ariaHidden"
  />
</template>

<script lang="ts">
import { defineComponent, reactive, PropType } from "vue";

export default defineComponent({
  name: "Icon",
  props: {
    name: { type: String, required: true },
    rotate: { type: Number as PropType<45 | 90 | 135 | 180 | 225 | 270 | 315> },
    flip: { type: String as PropType<"h" | "v"> },
    spin: { type: Boolean, default: false },
    ariaHidden: { type: Boolean, default: false },
    size: { type: Number, default: 1 },
  },
  setup(props) {
    const state = reactive({});
    const classes = ["reg-icon", "mdi", "mdi-" + props.name];
    if (props.rotate) classes.push("mdi-rotate-" + props.rotate);
    if (props.flip) classes.push("mdi-flip-" + props.flip);
    if (props.spin) classes.push("mdi-spin");
    return {
      state,
      classes,
    };
  },
});
</script>

<style lang="scss" scoped></style>
