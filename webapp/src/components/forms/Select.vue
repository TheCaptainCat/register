<template>
  <div class="reg-form reg-select-container" :class="{ fluid: fluid }">
    <label class="reg-select">
      <div class="reg-select-label">{{ label }}</div>
      <el-select
        :model-value="modelValue"
        @update:model-value="(value) => $emit('update:modelValue', value)"
      >
        <div v-for="item in options" :key="item.key">
          <el-option :label="item.label" :value="item.key" />
        </div>
      </el-select>
    </label>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "RegSelect",
  props: {
    name: {
      type: String,
      required: true,
    },
    modelValue: {
      type: String,
    },
    options: {
      type: Array as PropType<RegSelectOption[]>,
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
});

export interface RegSelectOption {
  key: string;
  label: string;
  value: string;
}
</script>

<style lang="scss" scoped></style>
