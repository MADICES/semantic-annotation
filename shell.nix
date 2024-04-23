{ pkgs ? (import <nixpkgs> {}) }:
pkgs.mkShell {
  packages = [
    pkgs.unzip
    pkgs.jq
  ];
}
