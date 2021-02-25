<template>
  <div class="reg-input-container">
    <label class="reg-input">
      <input
        :name="name"
        :class="hasValue ? ['has-value'] : []"
        :type="type"
        v-model="val"
      />
      <span v-if="label">{{ label }}</span>
    </label>
    <div v-if="error" class="error">
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
    error: String,
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
