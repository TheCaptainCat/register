import { reactive } from "vue";
import ApiRequest from "@/core/api";
import { HttpMethod } from "@/core/requests";
import Language from "@/composition/language/model";

export interface LanguageState {
  languages: Language[];
  loading: boolean;
}

const newLanguageState = (): LanguageState => {
  return reactive<LanguageState>({
    languages: [],
    loading: false,
  });
};

const getLanguages = async (state: LanguageState): Promise<void> => {
  state.loading = true;
  const request = new ApiRequest(HttpMethod.get, "/lang");
  const response = await request.fetch<Language[]>();
  state.languages = response.data;
  state.loading = false;
};

const createLanguage = async (
  state: LanguageState,
  name: string
): Promise<void> => {
  const request = new ApiRequest(HttpMethod.post, "/lang", { name });
  const response = await request.fetch<Language>();
  state.languages.push(response.data);
};

export { newLanguageState, getLanguages, createLanguage };
