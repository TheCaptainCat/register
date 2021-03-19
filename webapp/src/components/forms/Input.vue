<template>
  <div class="reg-form reg-input-container" :class="{ fluid: fluid }">
    <label>
      <div class="reg-input-label">{{ label }}</div>
      <el-input v-model="val" :placeholder="placeholder" />
    </label>
    <div v-if="error" class="reg-input-error">
      {{ error }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch, computed } from "vue";

export default defineComponent({
  name: "RegInput",
  props: {
    type: {
      type: String,
      default: "text",
    },
    name: {
      type: String,
      required: true,
    },
    modelValue: {
      type: String,
    },
    label: String,
    placeholder: String,
    error: String,
    fluid: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, context) {
    const val = ref<string | undefined>("");
    const hasValue = computed(() => val.value !== "");
    watch(val, () => {
      context.emit("update:modelValue", val.value);
    });
    watch(
      () => props.modelValue,
      () => {
        if (props.modelValue !== val.value) val.value = props.modelValue;
      }
    );
    return {
      val,
      hasValue,
    };
  },
});
</script>

<style lang="scss" scoped>
.reg-input-container {
  &.fluid {
    width: 100%;
  }

  .reg-input-label {
    font-weight: bold;
    margin-bottom: 3px;
  }

  .reg-input-error {
    color: red;
  }
}
</style>
