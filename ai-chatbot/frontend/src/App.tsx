import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import AuthPage from "./pages/AuthPage";
import ChatLayout from "./components/ChatLayout";
import ProtectedRoute from "./components/ProtectedRoute";

import {
  isAuthenticated,
} from "./services/api";


function App() {
  const authenticated =
    isAuthenticated();

  return (
    <Routes>

      <Route
        path="/login"
        element={
          authenticated ? (
            <Navigate
              to="/chat"
              replace
            />
          ) : (
            <AuthPage />
          )
        }
      />

      <Route
        path="/"
        element={
          <Navigate
            to={
              authenticated
                ? "/chat"
                : "/login"
            }
            replace
          />
        }
      />

      <Route element={<ProtectedRoute />}>

        <Route
          path="/chat"
          element={<ChatLayout />}
        />

      </Route>

      <Route
        path="*"
        element={
          <Navigate
            to={
              authenticated
                ? "/chat"
                : "/login"
            }
            replace
          />
        }
      />

    </Routes>
  );
}


export default App;