import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";

import type { CurrentUser } from "../types/chat";
import { logout } from "../services/api";

interface Props {
    user: CurrentUser;
}

export default function UserMenu({
    user,
}: Props) {
    const [open, setOpen] = useState(false);

    const menuRef =
        useRef<HTMLDivElement>(null);

    const navigate = useNavigate();

    useEffect(() => {
        function handleOutsideClick(
            event: MouseEvent
        ) {
            const target = event.target as Node;

            if (
                menuRef.current &&
                !menuRef.current.contains(target)
            ) {
                setOpen(false);
            }
        }

        document.addEventListener(
            "mousedown",
            handleOutsideClick
        );

        return () => {
            document.removeEventListener(
                "mousedown",
                handleOutsideClick
            );
        };
    }, []);

    function toggleMenu(
        event: React.MouseEvent<HTMLButtonElement>
    ) {
        event.preventDefault();
        event.stopPropagation();

        setOpen((previous) => !previous);
    }

    function handleLogout(
        event: React.MouseEvent<HTMLButtonElement>
    ) {
        event.preventDefault();
        event.stopPropagation();

        logout();

        setOpen(false);

        navigate("/login", {
            replace: true,
        });
    }

    return (
        <div
            ref={menuRef}
            className="user-menu"
        >
            <button
                type="button"
                className="user-profile-button"
                onClick={toggleMenu}
                aria-label="User profile"
                aria-expanded={open}
            >
                <div className="user-avatar">
                    {user.name
                        .charAt(0)
                        .toUpperCase()}
                </div>

                <span className="user-chevron">
                    {open ? "▴" : "▾"}
                </span>
            </button>

            {open && (
                <div
                    className="user-menu-dropdown"
                    onClick={(event) =>
                        event.stopPropagation()
                    }
                >
                    <div className="user-menu-header">
                        <strong>Name: {user.name}</strong><br />
                        <span>Email: {user.email}</span>
                    </div>

                    <div className="user-menu-divider" />

                    <button
                        type="button"
                        className="user-menu-item logout-item"
                        onClick={handleLogout}
                    >
                        ↪ Logout
                    </button>
                </div>
            )}
        </div>
    );
}