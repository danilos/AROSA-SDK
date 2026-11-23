# Example: consume an AROSA service

**AROSA**  
*Written for AROS*

Author: **DaniloS**. This is a **source-grounded integration pattern**, not a standalone compiled test.

In the public historical [AFileManager.Help.pas](https://github.com/danilos/AFileManager/blob/main/AFileManager.Help.pas), the application uses `Arosa.Services.Documentation` and `Arosa.Services.Presentation` instead of implementing help navigation and HTML display itself.

The following are actual declarations/logic from that application (adapted only to explanatory variable names):

```pascal
uses
  Arosa.Services.Documentation,
  Arosa.Services.Presentation;

{ In a class that already owns valid, initialized path and file services: }
Documentation := TArosaDocumentationService.CreateForApplication(
  PathService, FileService, BasePath, LanguageId);
try
  { Read an application-owned help topic through the shared service. }
  if Documentation.PageExists('index.html') then
  begin
    if Documentation.ReadText('index.html', PageText) then
      WriteLn('Loaded help page: ', Length(PageText), ' bytes');
  end;
finally
  Documentation.Free;
end;
```

### Required context

- `PathService` must be a valid `TArosaPathService`; `FileService` must be a valid `TArosaFileService`.
- `BasePath` names the application's package help root, `LanguageId` selects localization, and `PageText` is a `string`. Those values are supplied by the host application.
- Do **not** instantiate independent OS services if the platform has already supplied a compatible service instance. Follow the application's service registry and lifecycle.
- This fragment demonstrates the verified method names and arguments but **has not been separately compiled** against the historical SDK. The owning class in AFileManager uses inherited `TArosaObject` disposal semantics; ordinary `Free` behavior is to be confirmed for the installed SDK class.
- This example is deliberately limited to service consumption. Do not assume that a package's `.ppu` API is compatible with a different AROSA runtime version.

For a full application including UI forms, persistent workspaces, menus, context actions, sessions and services, read the public [AFileManager.pas](https://github.com/danilos/AFileManager/blob/main/AFileManager.pas) and [AFileManager.Help.pas](https://github.com/danilos/AFileManager/blob/main/AFileManager.Help.pas). Its private-platform build script is historical context, not a standalone SDK installer.
