# revision 25420
# category Package
# catalog-ctan /macros/latex/contrib/fixltxhyph
# catalog-date 2012-02-17 19:44:12 +0100
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-fixltxhyph
Version:	0.3
Release:	1
Summary:	Allow hyphenation of partially-emphasised substrings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixltxhyph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixltxhyph.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
