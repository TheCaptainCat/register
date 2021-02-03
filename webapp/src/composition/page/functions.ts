import ApiRequest from "@/core/api";
import { HttpMethod } from "@/core/requests";
import { reactive } from "vue";
import Page, { PartialPage } from "@/composition/page/models";

export interface PageState {
  page?: Page;
  loading: boolean;
}

export interface PageListState {
  pages: PartialPage[];
  loading: boolean;
}

const newPageState = (loading: boolean): PageState => {
  return reactive<PageState>({
    page: undefined,
    loading,
  });
};

const newPageListState = (loading: boolean): PageListState => {
  return reactive<PageListState>({
    pages: [],
    loading,
  });
};

const getPage = async (
  state: PageState,
  articleId: number,
  language: string
): Promise<void> => {
  state.loading = true;
  const request = new ApiRequest(
    HttpMethod.get,
    `/page/${language}/${articleId}`
  );
  const response = await request.fetch<Page>();
  state.page = response.data;
  state.loading = false;
};

const getPagesByLanguage = async (
  state: PageListState,
  language: string
): Promise<void> => {
  state.loading = true;
  const request = new ApiRequest(HttpMethod.get, `/page/${language}`);
  const response = await request.fetch<PartialPage[]>();
  state.pages = response.data;
  state.loading = false;
};

const addVersion = async (
  state: PageState,
  articleId: number,
  language: string,
  content: string
): Promise<void> => {
  const request = new ApiRequest(
    HttpMethod.patch,
    `/page/${language}/${articleId}`,
    {
      content,
    }
  );
  const response = await request.fetch<Page>();
  state.page = response.data;
};

const fetchContent = async (
  articleId: number,
  language: string
): Promise<void> => {
  const request = new ApiRequest(
    HttpMethod.get,
    `/page/${language}/${articleId}/content`
  );
  await request.fetch();
};

export {
  newPageState,
  newPageListState,
  getPage,
  getPagesByLanguage,
  addVersion,
  fetchContent,
};
