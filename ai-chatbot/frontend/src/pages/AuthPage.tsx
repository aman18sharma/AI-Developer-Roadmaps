import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
    login,
    register,
} from "../services/api";


export default function AuthPage() {
    const [isLogin, setIsLogin] =
        useState(true);

    const [name, setName] =
        useState("");

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [error, setError] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const navigate = useNavigate();


    async function handleSubmit(
        event: React.FormEvent
    ) {
        event.preventDefault();

        setError("");
        setLoading(true);

        try {
            if (isLogin) {
                await login(
                    email,
                    password
                );
            } else {
                await register(
                    name,
                    email,
                    password
                );

                await login(
                    email,
                    password
                );
            }

            navigate("/chat", {
                replace: true,
            });

        } catch (error) {
            setError(
                error instanceof Error
                    ? error.message
                    : "Authentication failed"
            );
        } finally {
            setLoading(false);
        }
    }


    return (
        <div className="auth-page">

            <div className="auth-card">

                <div className="auth-brand">
                    <div className="auth-logo">
                        BW
                    </div>

                    <span>Black &amp; White</span>
                </div>

                <div className="auth-heading">
                    <h1>
                        {isLogin
                            ? "Welcome back"
                            : "Create your account"}
                    </h1>

                    <p>
                        {isLogin
                            ? "Sign in to continue your conversations."
                            : "Create an account to get started."}
                    </p>
                </div>

                {error && (
                    <div className="auth-error">
                        {error}
                    </div>
                )}

                <form
                    onSubmit={handleSubmit}
                    className="auth-form"
                >

                    {!isLogin && (
                        <div className="form-field">
                            <label>Name</label>

                            <input
                                type="text"
                                value={name}
                                required
                                autoComplete="name"
                                onChange={(event) =>
                                    setName(
                                        event.target.value
                                    )
                                }
                                placeholder="Your name"
                            />
                        </div>
                    )}

                    <div className="form-field">
                        <label>Email</label>

                        <input
                            type="email"
                            value={email}
                            required
                            autoComplete="email"
                            onChange={(event) =>
                                setEmail(
                                    event.target.value
                                )
                            }
                            placeholder="you@example.com"
                        />
                    </div>

                    <div className="form-field">
                        <label>Password</label>

                        <input
                            type="password"
                            value={password}
                            required
                            minLength={8}
                            autoComplete={
                                isLogin
                                    ? "current-password"
                                    : "new-password"
                            }
                            onChange={(event) =>
                                setPassword(
                                    event.target.value
                                )
                            }
                            placeholder="••••••••"
                        />
                    </div>

                    <button
                        type="submit"
                        className="auth-submit"
                        disabled={loading}
                    >
                        {loading
                            ? "Please wait..."
                            : isLogin
                                ? "Sign in"
                                : "Create account"}
                    </button>

                </form>

                <div className="auth-switch">

                    <span>
                        {isLogin
                            ? "Don't have an account?"
                            : "Already have an account?"}
                    </span>

                    <button
                        type="button"
                        onClick={() => {
                            setIsLogin(
                                (value) => !value
                            );
                            setError("");
                        }}
                    >
                        {isLogin
                            ? "Sign up"
                            : "Sign in"}
                    </button>

                </div>

            </div>

        </div>
    );
}