import request from "@/core/api";
import { reactive } from "vue";

// MODEL

interface Article {
  name: string;
  language: string;
  article: string;
}

// ARTICLE METHODS

const create = async (lang: string, name: string): Promise<Article> => {
  const res = await request.post<{ name: string }, Article>(`/page/${lang}`, {
    name,
  });
  return res.data;
};

// USE ARTICLE

interface UseArticleParams {
  create: (lang: string, name: string) => Promise<Article>;
}

const useArticle = (): UseArticleParams => {
  return {
    create,
  };
};

// ARTICLES METHODS

const getFromLang = async (lang: string): Promise<Article[]> => {
  const res = await request.get<Article[]>(`/page/${lang}`);
  return res.data;
};

// USE ARTICLES

interface ArticlesState {
  articles: Article[];
  loading: boolean;
}

interface UseArticlesParams {
  state: ArticlesState;
  getFromLang: (lang: string) => Promise<Article[]>;
}

const useArticles = (): UseArticlesParams => {
  return {
    state: reactive({ articles: [], loading: false }),
    getFromLang,
  };
};

export { Article, useArticle, useArticles };
