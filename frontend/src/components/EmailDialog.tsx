import { useEffect, useRef, useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "./ui/dialog";
import { Label } from "./ui/label";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { USER } from "@/hooks/useUser";
import { createUser } from "@/lib/api";
import { useQueryClient } from "@tanstack/react-query";

const EmailDialog = () => {
  const [open, setOpen] = useState(() => {
    if (typeof window === "undefined") return true;
    return !localStorage.getItem("user_id");
  });
  // fields state
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  // errors object
  const [errors, setErrors] = useState<{ name: string; email: string }>({
    name: "",
    email: "",
  });

  const firstRef = useRef<HTMLInputElement>(null);
  const secondRef = useRef<HTMLInputElement>(null);

  const qc = useQueryClient();

  useEffect(() => {
    if (typeof window === "undefined") return;
    if (localStorage.getItem("user_id")) {
      setOpen(false);
    }
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    // prevents default behavior like reloading the page
    e.preventDefault();
    // reset the errors, it's a new form submission
    setErrors({ name: "", email: "" });

    // manual validation
    if (!email.includes("@")) {
      setErrors({ ...errors, email: "Email must include an @" });
      return;
    }

    if (name.length < 1) {
      setErrors({ ...errors, name: "Name must be at least 1 character" });
      return;
    }

    const payload = {
      name,
      email,
    };

    try {
      const createdUser = await createUser(payload);
      qc.setQueryData([USER], createdUser);
      localStorage.setItem("user_id", createdUser.id);
    } catch (error) {
      console.error("Error creating user", error);
      return;
    }

    console.log("Form Submitted!");
    setOpen(false);
  };

  // const exists = localStorage.getItem("user_id") !== null;
  // setOpen(!exists)

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogContent
        className="sm:max-w-[425px]"
        showCloseButton={false}
        onInteractOutside={(e) => e.preventDefault()}
        onEscapeKeyDown={(e) => e.preventDefault()}
      >
        <DialogHeader>
          <DialogTitle>Start your demo</DialogTitle>
          <DialogDescription>
            Enter your name and email to begin.
          </DialogDescription>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="grid gap-4">
          <div className="grid gap-4">
            <div className="grid gap-3">
              <Label htmlFor="name">Name</Label>
              <Input
                ref={firstRef}
                onKeyDown={(e: React.KeyboardEvent<HTMLInputElement>) => {
                  if (e.key === "Enter") {
                    e.preventDefault();
                    secondRef.current?.focus();
                  }
                }}
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="John Smith"
              />
              {errors.name && <p className="text-red-400">{errors.name}</p>}
            </div>
            <div className="grid gap-3">
              <Label htmlFor="email-1">Email</Label>
              <Input
                ref={secondRef}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="johnsmith@example.com"
              />
              {errors.email && <p className="text-red-400">{errors.email}</p>}
            </div>
          </div>
          <DialogFooter>
            <Button type="submit" disabled={!name || !email}>
              Continue
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default EmailDialog;
