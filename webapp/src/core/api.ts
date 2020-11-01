import FetchRequest, { HttpMethod } from "@/core/requests";
import Env from "@/core/env";

export default class ApiRequest<T> extends FetchRequest<T> {
  constructor(method: HttpMethod, path: string, body?: T) {
    super(method, Env.API_URL, path, body);
  }
}
