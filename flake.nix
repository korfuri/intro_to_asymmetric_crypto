{
  description = "Interactive presentation, an introduction to cryptography";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05-small";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  outputs = { self, nixpkgs, flake-utils }: flake-utils.lib.eachDefaultSystem (system: let
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.default = pkgs.mkShell {
      buildInputs = [
        pkgs.mdp
        pkgs.python3
        pkgs.openssl
      ];
    };
  });
}
