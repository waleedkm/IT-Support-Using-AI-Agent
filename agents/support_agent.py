def handle_support(query):
    if "password" in query:
        return "Password reset link sent to your email."
    elif "install" in query:
        return "Software installation started."
    return "Issue not recognized."
