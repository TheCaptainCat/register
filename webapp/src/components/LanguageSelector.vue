<template>
  <div class="language-selector">
    <div v-for="lang in state.languages" :key="lang" class="lang-icon">
      <span
        :class="['flag-icon', `flag-icon-${i18n.flags[lang]}`]"
        @click="i18n.changeLocale(lang)"
      ></span>
    </div>
  </div>
</template>

<script lang="ts">
import "flag-icon-css/css/flag-icon.min.css";

import { defineComponent, reactive } from "vue";
import { useI18n } from "@/plugins/i18n";
import { stringComparator } from "@/utils/strings";

export default defineComponent({
  name: "LanguageSelector",
  setup() {
    const i18n = useI18n();
    const state = reactive({
      languages: Object.keys(i18n.messages)
        .map((k) => k)
        .sort(stringComparator),
    });
    return {
      i18n,
      state,
    };
  },
});
</script>

<style lang="scss" scoped>
.language-selector {
  display: flex;

  .lang-icon {
    margin-right: 15px;
    font-size: 1.5rem;
    cursor: pointer;
  }

  .lang-icon:last-of-type {
    margin-right: 0;
  }
}
</style>
