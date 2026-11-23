// Copyright (c) 2026 DaniloS
// AROSA SDK introductory example; supplied as example source.
// Compile against the historical, architecture-matched AROSA SDK.
// This example has not been independently compiled or run.
program HelloAROSA;

{$mode objfpc}{$H+}

uses
  SysUtils,
  Arosa.Version;

begin
  WriteLn('Hello from an AROSA SDK consumer.');
  WriteLn('AROSA.Version unit resolved from the SDK if compilation succeeds.');
end.
