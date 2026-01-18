import { useEffect, useRef, useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "./ui/dialog";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { USER } from "@/hooks/useUser";
import { createUser } from "@/lib/api";
import { useQueryClient } from "@tanstack/react-query";
import { Field, FieldGroup, FieldLabel, FieldSeparator } from "./ui/field";

type EmailDialogProps = { onUserCreated?: (id: string) => void };

const EmailDialog = ({ onUserCreated }: EmailDialogProps) => {
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
      onUserCreated?.(createdUser.id);
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
        className="sm:max-w-[425px] grid gap-6"
        showCloseButton={false}
        onInteractOutside={(e) => e.preventDefault()}
        onEscapeKeyDown={(e) => e.preventDefault()}
      >
        <DialogHeader>
          <DialogTitle>Start your demo</DialogTitle>
          <DialogDescription>
            Login with your Google account
          </DialogDescription>
        </DialogHeader>
        {/* <form onSubmit={handleSubmit} className="grid gap-4">
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
        </form> */}
        <form onSubmit={handleSubmit}>
          <FieldGroup>
            <Field>
              <Button variant="outline" type="button">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path
                    d="M12.48 10.92v3.28h7.84c-.24 1.84-.853 3.187-1.787 4.133-1.147 1.147-2.933 2.4-6.053 2.4-4.827 0-8.6-3.893-8.6-8.72s3.773-8.72 8.6-8.72c2.6 0 4.507 1.027 5.907 2.347l2.307-2.307C18.747 1.44 16.133 0 12.48 0 5.867 0 .307 5.387.307 12s5.56 12 12.173 12c3.573 0 6.267-1.173 8.373-3.36 2.16-2.16 2.84-5.213 2.84-7.667 0-.76-.053-1.467-.173-2.053H12.48z"
                    fill="currentColor"
                  />
                </svg>
                Login with Google
              </Button>
            </Field>
            <FieldSeparator>Or continue with</FieldSeparator>
            <Field>
              <FieldLabel htmlFor="name">Name</FieldLabel>
              <Input
                ref={firstRef}
                onKeyDown={(e: React.KeyboardEvent<HTMLInputElement>) => {
                  if (e.key === "Enter") {
                    e.preventDefault();
                    secondRef.current?.focus();
                  }
                }}
                placeholder="John Smith"
                value={name}
                onChange={(e) => setName(e.target.value)}
              ></Input>
              {errors.name && <p className="text-red-400">{errors.name}</p>}
            </Field>
            <Field>
              <FieldLabel htmlFor="email">Email</FieldLabel>
              <Input
                ref={secondRef}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="johnsmith@example.com"
              />
              {errors.email && <p className="text-red-400">{errors.email}</p>}
            </Field>
            <Field>
              <Button type="submit" disabled={!name || !email}>
                Continue
              </Button>
            </Field>
          </FieldGroup>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default EmailDialog;
