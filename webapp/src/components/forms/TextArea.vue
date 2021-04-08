<template>
  <div class="reg-form reg-input-container">
    <label>
      <div class="reg-input-label">{{ label }}</div>
      <el-input
        type="textarea"
        v-model="val"
        :placeholder="placeholder"
        :autosize="autosize"
      />
    </label>
    <div v-if="error" class="reg-input-error">
      {{ error }}
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, PropType, ref, watch } from "vue";

export default defineComponent({
  name: "RegTextArea",
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
    dimensions: {
      type: Object as PropType<{ min?: number; max?: number }>,
    },
  },
  setup(props, context) {
    const val = ref<string | undefined>(props.modelValue);
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
  computed: {
    autosize() {
      if (!this.dimensions) return {};
      let size: { minRows?: number; maxRows?: number } = {};
      if ("min" in this.dimensions) size.minRows = this.dimensions.min;
      if ("max" in this.dimensions) size.maxRows = this.dimensions.max;
      return size;
    },
  },
});
</script>

<style lang="scss" scoped></style>
