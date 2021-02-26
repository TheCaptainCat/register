import { provide, inject, ref, Ref } from "vue";
import AppStorage from "@/core/storage";

type LangDefinition = Record<string, string | object>;
type LangStrings = Record<string, string>;

interface I18n {
  locale: Ref<string>;
  defaultLocale: string;
  messages: Record<string, LangStrings>;
  t: (key: string) => string;
  changeLocale: (lang: string) => void;
}

class LanguageStorage extends AppStorage<{ language: string }> {
  public constructor() {
    super("language");
  }
}

const languageStorage = new LanguageStorage();

const parseStrings = (prefix: string, node: LangDefinition): LangStrings => {
  const strings: LangStrings = {};
  for (const key in node) {
    const value = node[key];
    if (typeof value === "string") {
      strings[prefix + key] = value;
    } else {
      const substrings = parseStrings(
        prefix + key + ".",
        value as LangDefinition
      );
      for (const subKey in substrings) {
        strings[subKey] = substrings[subKey];
      }
    }
  }
  return strings;
};

const buildI18nStrings = (
  languages: Record<string, LangDefinition>
): Record<string, LangStrings> => {
  const built: Record<string, LangStrings> = {};
  for (const lang in languages) {
    built[lang] = parseStrings("", languages[lang]);
  }
  return built;
};

const createI18n = (
  config: Record<string, LangDefinition>,
  lang: string,
  defaultLocale: string
): I18n => ({
  locale: ref(lang),
  defaultLocale,
  messages: buildI18nStrings(config),
  t(key) {
    if (key in this.messages[this.locale.value]) {
      return this.messages[lang][key];
    } else if (key in this.messages[this.defaultLocale]) {
      return this.messages[this.defaultLocale][key];
    }
    return key;
  },
  changeLocale(lang) {
    this.locale.value = lang;
  },
});

const i18nSymbol = Symbol();

function provideI18n(
  i18nConfig: Record<string, LangDefinition>,
  defaultLang: string
): void {
  let lang = defaultLang;
  const storedLang = languageStorage.get();
  if (storedLang !== null) {
    lang = storedLang.language;
  }
  const i18n = createI18n(i18nConfig, lang, defaultLang);
  provide(i18nSymbol, i18n);
}

function useI18n(): I18n {
  const i18n = inject<I18n>(i18nSymbol);
  if (!i18n) throw new Error("No i18n provided");
  return i18n;
}

export { provideI18n, useI18n };
