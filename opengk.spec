Summary:	H.323 basic gatekeeper
Summary(pl):	Podstawowy gatekeeper H.323
Name:		opengk
Version:	1.13.5
%define fver	%(echo %{version} | tr . _)
Release:	1
License:	MPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src.tar.gz
# Source0-md5:	714bef61405413dc40ea23a4d12dc592
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-mak_files.patch
Patch2:		%{name}-openh323.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.17
BuildRequires:	pwlib-devel >= 1.8
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very basic H.323 Gatekeeper.

Basic features OpenGatekeeper supports all the basic features of an
H.323 Gatekeeper such as registration, admissions and access control,
address translation and bandwidth monitoring and control.

Advanced features:
- Gatekeeper routed calls
- Support of H.323v2 alias types (party number, URL, transport id and
  email address)
- Support for gateway prefixes
- Registration and call activity logs
- Neighbour gatekeeper database
- Registration time to live

%description -l pl
To jest podstawowy Gatekeeper H.323.

OpenGatekeeper obs³uguje podstawowe mo¿liwo¶ci Gatekeepera H.323, takie
jak rejestracja, przyjmowanie, kontrola dostêpu, t³umaczenie adresów,
monitorowanie i kontrola pasma.

Zaawansowane mo¿liwo¶ci:
- routowane po³±czenia
- wsparcie dla typów aliasów H.323v2 (numer, URL, transport id, adres
  e-mail)
- obs³uga przedrostków bramek
- logowanie rejestracji i po³±czeñ
- baza danych s±siednich gatekeeperów
- czas obowi±zywania rejestracji.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} %{?debug:debug}%{!?debug:opt}shared \
	CXX="%{__cxx}" \
	OPTCCFLAGS="%{rpmcflags} -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
