import { ref, provide, inject, Ref } from "vue";
import AppStorage from "@/core/storage";

type LangDefinition = Record<string, string | object>;
type LangStrings = Record<string, string>;

interface I18n {
  locale: Ref<string>;
  defaultLocale: string;
  messages: Record<string, LangStrings>;
  t: (key: string, params?: Record<string, unknown>) => string;
  changeLocale: (lang: string) => void;
}

class LocaleStorage extends AppStorage<{ lang: string }> {
  constructor() {
    super("locale");
  }
}

const localeStorage = new LocaleStorage();

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

const replaceParams = (str: string, params?: Record<string, unknown>) => {
  if (params)
    for (const key in params) {
      const regex = new RegExp(`{ *${key} *}`);
      str = str.replace(regex, params[key] as string);
    }
  return str;
};

const createI18n = (
  locale: string,
  defaultLocale: string,
  messages: Record<string, LangStrings>
): I18n => ({
  locale: ref(locale),
  defaultLocale,
  messages,
  t(key, params) {
    if (key in this.messages[this.locale.value])
      return replaceParams(this.messages[this.locale.value][key], params);
    if (
      this.locale.value !== this.defaultLocale &&
      key in this.messages[this.defaultLocale]
    )
      return replaceParams(this.messages[this.defaultLocale][key], params);
    return key;
  },
  changeLocale(lang) {
    localeStorage.set({ lang: lang });
    this.locale.value = lang;
  },
});

const i18nSymbol = Symbol();

const provideI18n = (
  defaultLocale: string,
  messages: Record<string, LangStrings>
): void => {
  let lang = defaultLocale;
  const storedLocale = localeStorage.get();
  if (storedLocale) lang = storedLocale.lang;
  else localeStorage.set({ lang });
  const i18n = createI18n(lang, defaultLocale, messages);
  provide(i18nSymbol, i18n);
};

const useI18n = (): I18n => {
  const i18n = inject<I18n>(i18nSymbol);
  if (!i18n) throw new Error("Internal Error: no i18n provided");
  return i18n;
};

export { I18n, buildI18nStrings, provideI18n, useI18n };
