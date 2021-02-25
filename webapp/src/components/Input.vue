<template>
  <div class="reg-input-container">
    <label class="reg-input">
      <input
        :class="hasValue ? ['has-value'] : []"
        :type="type"
        v-model="val"
      />
      <span v-if="label">{{ label }}</span>
    </label>
    <div v-if="error" class="error">
      {{ $t("components.input.errors." + error) }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch, computed } from "vue";

export default defineComponent({
  name: "Input",
  props: {
    type: {
      type: String,
      default: "text",
    },
    modelValue: {
      type: String,
      required: true,
    },
    label: String,
    error: String,
  },
  setup(props, context) {
    const val = ref("");
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
