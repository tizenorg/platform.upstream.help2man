Name:           help2man
Version:        1.40.10
Release:        0
License:        GPL-3.0+
Summary:        Create Simple Man Pages from --help Output
Url:            http://www.gnu.org/software/help2man/
Group:          Development/Tools/Doc Generators
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gettext-tools
BuildRequires:  perl-gettext
Requires:       perl-gettext

%description
help2man is a script to create simple man pages from the --help and
--version output of programs.

Since most GNU documentation is now in info format, this provides a way
to generate a placeholder man page pointing to that resource while
still providing some useful information.

%prep
%setup -q

%build
%configure --enable-nls
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name} --with-man


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING 
%{_bindir}/help2man
%{_libdir}/help2man/
%doc %{_infodir}/help2man.info%{ext_info}
%doc %{_mandir}/man1/help2man.1%{ext_man}
%dir %{_mandir}/??
%dir %{_mandir}/??/man1

%changelog
