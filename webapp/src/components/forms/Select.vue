<template>
  <div class="reg-input-container" :class="{ fluid: fluid }">
    <label class="reg-input">
      <select
        class="reg-input-elem"
        :class="{ 'has-value': hasValue }"
        v-model="val"
        @change="val = $event.target.value"
        :disabled="disabled"
      >
        <option v-for="option in options" :key="option.key" :value="option.key">
          {{ option.label }}
        </option>
      </select>
      <span v-if="label">{{ label }}</span>
    </label>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, PropType, ref, watch } from "vue";

export default defineComponent({
  name: "RegSelect",
  props: {
    name: {
      type: String,
      required: true,
    },
    modelValue: {
      type: Object as PropType<RegSelectOption<unknown>>,
    },
    options: {
      type: Array as PropType<RegSelectOption<unknown>[]>,
    },
    label: String,
    error: String,
    fluid: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, context) {
    const val = ref<string>("");
    const hasValue = computed(() => val.value !== "");
    watch(val, () => {
      let value = null;
      if (props.options) {
        const res = props.options.filter((o) => o.key === val.value);
        if (res && res.length) value = res[0];
      }
      context.emit("update:modelValue", value);
    });
    watch(
      () => props.modelValue,
      () => {
        if (!props.modelValue) val.value = "";
        else if (props.modelValue.key !== val.value)
          val.value = props.modelValue.key;
      }
    );
    const clickOption = (value: string) => {
      val.value = value;
    };
    return {
      val,
      hasValue,
      clickOption,
    };
  },
});

export interface RegSelectOption<T> {
  key: string;
  label: string;
  value: T;
}
</script>

<style lang="scss" scoped></style>
