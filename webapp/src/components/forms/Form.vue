<template>
  <div :id="`reg-form-${uid}`" class="reg-form-container" :class="{ inline }">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegForm",
  props: {
    inline: { type: Boolean, default: false },
  },
  mounted() {
    const elem = document.getElementById(`reg-form-${this.uid}`);
    if (elem) elem.addEventListener("keyup", this.submit);
  },
  beforeUnmount() {
    const elem = document.getElementById(`reg-form-${this.uid}`);
    if (elem) elem.removeEventListener("keyup", this.submit);
  },
  setup(props, context) {
    let uid = Math.random().toString(36).substring(7);
    const submit = (e: KeyboardEvent) => {
      if (["Enter", "NumpadEnter"].includes(e.code)) context.emit("submit");
    };
    return {
      submit,
      uid,
    };
  },
});
</script>

<style lang="scss" scoped>
.reg-form-container {
  width: 100%;
  display: flex;
  &.inline {
    flex-direction: row;
    ::v-deep .reg-form:not(:last-child) {
      margin-right: 5px;
    }
  }
  &:not(.inline) {
    flex-direction: column;
    ::v-deep .reg-form:not(:last-child) {
      margin-bottom: 15px;
    }
  }
}
</style>
