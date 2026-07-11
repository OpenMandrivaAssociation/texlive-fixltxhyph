%global tl_name fixltxhyph
%global tl_revision 73227

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Allow hyphenation of partially-emphasised substrings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixltxhyph
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package fixes the problem of TeX failing to hyphenate letter strings
that seem (to TeX) to be words, but which are followed by an apostrophe
and then an emphasis command. The cause of the problem is not the
apostrophe, but the font change in the middle of the string. The problem
arises in Catalan, French, Italian and Romansh.

