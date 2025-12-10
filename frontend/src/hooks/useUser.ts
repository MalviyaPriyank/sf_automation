import { getUser, type User } from "@/lib/api";
import { useQuery } from "@tanstack/react-query";
import { useEffect } from "react";

export const USER = "user";

const useUser = () => {
  const userId = typeof window !== "undefined" ? localStorage.getItem("user_id") : null;
  const { data: user, isError, ...rest } = useQuery<User>({
    queryKey: [USER],
    queryFn: () => getUser(userId!),
    enabled: !!userId,
    refetchOnWindowFocus: false,
    retry: false,
  });

  useEffect(() => {
    if (isError && typeof window !== "undefined") {
      localStorage.removeItem("user_id");
    }
  }, [isError]);

  return {
    user,
    isError,
    ...rest,
  };
};

export default useUser;
