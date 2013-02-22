Summary:	BS2B (Bauer stereophonic-to-binaural DSP) effect plugin for XMMS
Summary(pl.UTF-8):	Wtyczka efektu BS2B (DSP stereofoniczno-dwuusznego Bauera) jak wtyczka efektu XMMS-a
Name:		xmms-effect-bs2b
Version:	0.5.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/bs2b/xmms-bs2b-%{version}.tar.lzma
# Source0-md5:	4a676bbb4aa8efeffd36ec690ca26960
URL:		http://modplug-xmms.sourceforge.net/
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libbs2b-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.0.0
Requires:	libbs2b >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BS2B (Bauer stereophonic-to-binaural DSP) effect plugin for XMMS.

%description -l pl.UTF-8
Wtyczka efektu BS2B (DSP stereofoniczno-dwuusznego Bauera) jak wtyczka
efektu XMMS-a.

%prep
%setup -q -n xmms-bs2b-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{xmms_effect_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{xmms_effect_plugindir}/libxmmsbs2b.so
