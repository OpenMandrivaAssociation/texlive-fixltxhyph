Name:		texlive-fixltxhyph
Version:	25832
Release:	2
Summary:	Allow hyphenation of partially-emphasised substrings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixltxhyph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package fixes the problem of TeX failing to hyphenate
letter strings that seem (to TeX) to be words, but which are
followed by an apostrophe and then an emphasis command. The
cause of the problem is not the apostrophe, but the font change
in the middle of the string. The problem arises in Catalan,
French and Italian (it could arise in Romansh, were there LaTeX
support for it).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fixltxhyph/fixltxhyph.sty
%doc %{_texmfdistdir}/doc/latex/fixltxhyph/README
%doc %{_texmfdistdir}/doc/latex/fixltxhyph/fixltxhyph.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fixltxhyph/fixltxhyph.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
