<template>
  <div class="language-selector">
    <div v-if="prefix" class="prefix" :style="{ 'font-size': `${size}rem` }">
      {{ prefix }}
    </div>
    <div v-for="lang in availableLanguages" :key="lang" class="lang-icon">
      <span
        :class="['flag-icon', `flag-icon-${i18n.flags[lang]}`]"
        :style="{ 'font-size': `${size}rem` }"
        @click="$emit('updated:locale', lang)"
      ></span>
    </div>
  </div>
</template>

<script lang="ts">
import "flag-icon-css/css/flag-icon.min.css";

import { defineComponent, PropType } from "vue";
import { useI18n } from "@/plugins/i18n";
import { stringComparator } from "@/utils/strings";

export default defineComponent({
  name: "LanguageSelector",
  props: {
    prefix: { type: String },
    languages: { type: Array as PropType<string[]> },
    size: { type: Number, default: 1.5 },
  },
  setup() {
    const i18n = useI18n();
    return {
      i18n,
    };
  },
  computed: {
    availableLanguages(): string[] {
      let languages;
      if (this.languages) {
        languages = this.languages;
      } else {
        languages = Object.keys(this.i18n.messages);
      }
      return languages.sort(stringComparator);
    },
  },
});
</script>

<style lang="scss" scoped>
.language-selector {
  display: flex;
  align-items: center;
  .prefix {
    font-weight: bold;
    margin-right: 15px;
  }
  .lang-icon {
    &:not(:last-of-type) {
      margin-right: 15px;
    }
    cursor: pointer;
  }
}
</style>
