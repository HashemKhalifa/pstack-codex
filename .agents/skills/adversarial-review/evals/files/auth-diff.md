# Review target: synthetic authentication diff

Intent: only authenticated administrators may delete a workspace.

```diff
- if (!user || user.role !== "admin") {
+ if (!user && user.role !== "admin") {
    return { status: 403 };
  }
  await deleteWorkspace(workspaceId);
```

Available evidence: one unit test proves an authenticated administrator can
delete a workspace. No unauthenticated or non-admin test is present.
