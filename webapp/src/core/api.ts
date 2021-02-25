import FetchRequest, { FetchResponse } from "@/core/requests";
import Env from "@/core/env";

class ApiRequest {
  public async get<Rs>(path: string): Promise<FetchResponse<Rs>> {
    const request = new FetchRequest("GET", Env.API_URL, path);
    return await request.fetch<Rs>();
  }

  public async post<Rq, Rs>(
    path: string,
    body: Rq
  ): Promise<FetchResponse<Rs>> {
    const request = new FetchRequest<Rq>("POST", Env.API_URL, path, body);
    return await request.fetch<Rs>();
  }

  public async put<Rq, Rs>(path: string, body: Rq): Promise<FetchResponse<Rs>> {
    const request = new FetchRequest<Rq>("PUT", Env.API_URL, path, body);
    return await request.fetch<Rs>();
  }

  public async patch<Rq, Rs>(
    path: string,
    body: Rq
  ): Promise<FetchResponse<Rs>> {
    const request = new FetchRequest<Rq>("PATCH", Env.API_URL, path, body);
    return await request.fetch<Rs>();
  }

  public async delete<Rs>(path: string): Promise<FetchResponse<Rs>> {
    const request = new FetchRequest("DELETE", Env.API_URL, path);
    return await request.fetch<Rs>();
  }
}

const request = new ApiRequest();

export default request;
