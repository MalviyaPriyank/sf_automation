import API from "@/config/apiClient";

export type User = {
  id: string;
  name: string;
  email: string;
};

export type Conversation = {
  _id: string;
  userId: string;
  title: string;
};

export type CreateUserPayload = Omit<User, "id">;

export const getUser = (userId: string) =>
  API.get<User>("/user", { params: { user_id: userId } }).then(
    (res) => res.data
  );

export const createUser = (payload: CreateUserPayload) =>
  API.post<User>("/user", payload).then((res) => res.data);

export const getConversations = (userId: string) =>
  API.get<Conversation[]>("/conversation", {
    params: { user_id: userId },
  }).then((res) => res.data);

export const deleteConversations = (id: Conversation["_id"]) =>
  API.delete(`/conversation/${id}`);
